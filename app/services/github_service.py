import httpx
from app.core.config import GITHUB_TOKEN

BASE_URL = "https://api.github.com"


async def fetch_issue(owner: str, repo: str, issue_number: int):

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    url = f"{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    return response.json()