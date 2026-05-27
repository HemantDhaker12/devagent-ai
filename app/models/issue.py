from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base


class IssueMemory(Base):

    __tablename__ = "issue_memory"

    id = Column(Integer, primary_key=True, index=True)

    github_issue_id = Column(String, unique=True)

    title = Column(String)
    body = Column(Text)

    summary = Column(Text)
    severity = Column(String)
    issue_type = Column(String)

    root_cause = Column(Text)

    confidence = Column(String)