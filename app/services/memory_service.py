from sqlalchemy.orm import Session
from app.models.issue import IssueMemory


def store_issue_analysis(
    db: Session,
    github_issue_id: str,
    title: str,
    body: str,
    analysis: dict
):

    new_issue = IssueMemory(
        github_issue_id=github_issue_id,
        title=title,
        body=body,
        summary=analysis["summary"],
        severity=analysis["severity"],
        issue_type=analysis["type"],
        root_cause=analysis["root_cause"],
        confidence=analysis["confidence"]
    )

    db.add(new_issue)
    db.commit()
    print("Issue analysis stored successfully")
    db.refresh(new_issue)

    return new_issue