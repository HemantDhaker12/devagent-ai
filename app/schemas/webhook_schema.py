from pydantic import BaseModel


class RepositoryOwner(BaseModel):
    login: str


class Repository(BaseModel):
    name: str
    owner: RepositoryOwner


class Issue(BaseModel):
    number: int
    title: str
    body: str | None = None


class GitHubWebhookPayload(BaseModel):
    action: str
    issue: Issue
    repository: Repository