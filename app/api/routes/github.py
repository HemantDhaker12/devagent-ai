from fastapi import APIRouter
from app.schemas.webhook_schema import (
    GitHubWebhookPayload
)

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)


@router.post("/github")
async def github_webhook(
    payload: GitHubWebhookPayload
):

    return {
        "message": "Webhook received",
        "payload": payload.model_dump()
    }