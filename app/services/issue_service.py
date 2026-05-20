from app.services.github_service import fetch_issue
from app.agents.issue_agent import analyze_issue_with_ai


async def analyze_github_issue(owner, repo, issue_number):

    issue_data = await fetch_issue(owner, repo, issue_number)

    title = issue_data.get("title", "")
    body = issue_data.get("body", "")

    ai_response = await analyze_issue_with_ai(title, body)

    return {
        "github_issue": {
            "title": title,
            "body": body,
            "state": issue_data.get("state")
        },
        "analysis": ai_response
    }