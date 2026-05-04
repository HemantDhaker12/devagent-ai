from fastapi import FastAPI
from app.api.routes import health, issue

app = FastAPI(title="DevAgent")

app.include_router(health.router)
app.include_router(issue.router)