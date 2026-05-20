from fastapi import APIRouter
from app.services.issue_service import analyze_github_issue

router = APIRouter(prefix="/issue", tags=["Issue"])


@router.get("/{owner}/{repo}/{issue_number}")
async def analyze_issue(owner: str, repo: str, issue_number: int):

    return await analyze_github_issue(
        owner,
        repo,
        issue_number
    )