from sqlalchemy.orm import Session
from app.models.issue import IssueMemory


def store_issue_analysis(
    db: Session,
    github_issue_id: str,
    title: str,
    body: str,
    analysis: dict
):

    existing_issue = (
        db.query(IssueMemory)
        .filter(
            IssueMemory.github_issue_id == github_issue_id
        )
        .first()
    )

    # UPDATE existing issue
    if existing_issue:

        existing_issue.title = title
        existing_issue.body = body
        existing_issue.summary = analysis["summary"]
        existing_issue.severity = analysis["severity"]
        existing_issue.issue_type = analysis["type"]
        existing_issue.root_cause = analysis["root_cause"]
        existing_issue.confidence = analysis["confidence"]

        db.commit()
        db.refresh(existing_issue)

        return existing_issue

    # CREATE new issue
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
    db.refresh(new_issue)

    return new_issue