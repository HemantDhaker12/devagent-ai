from app.models.issue import IssueMemory
from fastapi import APIRouter
from app.services.issue_service import analyze_github_issue
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db

router = APIRouter(prefix="/issue", tags=["Issue"])


@router.get("/{owner}/{repo}/{issue_number}")
async def analyze_issue(owner: str, repo: str, issue_number: int, db: Session = Depends(get_db)):

    return await analyze_github_issue(
        owner,
        repo,
        issue_number,
        db
    )

from app.services.rag_service import (
    store_issue_memory,
    retrieve_similar_issues
)

@router.get("/memory/test")
async def test_memory():

    store_issue_memory(
        "1",
        "FastAPI authentication issue with JWT token"
    )

    results = retrieve_similar_issues(
        "JWT authentication problem"
    )

    return results

@router.get("/memory/all")
async def get_all_memory(db: Session = Depends(get_db)):

    return db.query(IssueMemory).all()