from app.services.github_service import fetch_issue
from app.agents.issue_agent import analyze_issue_with_ai
from app.schemas.issue_schema import IssueAnalysisResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.rag_service import (
    retrieve_similar_issues,
    store_issue_memory
)
from app.services.memory_service import (
    store_issue_analysis
)



async def analyze_github_issue(owner, repo, issue_number,db):

    issue_data = await fetch_issue(owner, repo, issue_number)

    title = issue_data.get("title", "")
    body = issue_data.get("body", "")

    query_text = f"{title} {body}"

    similar_results = retrieve_similar_issues(query_text)

    similar_docs = similar_results.get(
        "documents",
        [[]]
    )[0]

    similar_issues = "\n".join(similar_docs)

    ai_response = await analyze_issue_with_ai(
        title,
        body,
        similar_issues
    )

    store_issue_memory(
        str(issue_number),
        query_text
    )

    validated_response = IssueAnalysisResponse(
        **ai_response
    )
    

    store_issue_analysis(
        db=db,
        github_issue_id=str(issue_number),
        title=title,
        body=body,
        analysis=validated_response.model_dump()
    )

    return {
        "github_issue": {
            "title": title,
            "body": body,
            "state": issue_data.get("state")
        },
        "similar_issues": similar_docs,
        "analysis": validated_response.model_dump()
    }