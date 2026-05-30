from fastapi import APIRouter

from app.services.webhook_service import process_github_issue_webhook

from app.schemas.webhook_schema import (
    GitHubWebhookPayload
)

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)


@router.post("/github")
async def github_webhook(payload: GitHubWebhookPayload):

    return await process_github_issue_webhook(payload)