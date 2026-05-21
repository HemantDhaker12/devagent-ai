from pydantic import BaseModel
from typing import List


class IssueAnalysisResponse(BaseModel):
    summary: str
    type: str
    severity: str
    root_cause: str
    suggested_fix: List[str]
    confidence: str