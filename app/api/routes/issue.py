from fastapi import APIRouter

router = APIRouter(prefix="/issue", tags=["Issue"])

@router.post("/analyze")
async def analyze_issue():
    return {
        "message": "Issue analyzer endpoint working"
    }