from app.services.github_service import fetch_issue
from app.agents.issue_agent import analyze_issue_with_ai
from app.schemas.issue_schema import IssueAnalysisResponse


async def analyze_github_issue(owner, repo, issue_number):

    issue_data = await fetch_issue(owner, repo, issue_number)

    title = issue_data.get("title", "")
    body = issue_data.get("body", "")

    ai_response = await analyze_issue_with_ai(title, body)

    validated_response = IssueAnalysisResponse(**ai_response)

    return {
        "github_issue": {
            "title": title,
            "body": body,
            "state": issue_data.get("state")
        },
        "analysis": validated_response.model_dump()
    }