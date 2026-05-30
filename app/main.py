from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

from app.api.routes import auth, issue

from app.models import user
from app.models import issue as issue_model
from app.api.routes import github

app = FastAPI()

app.include_router(auth.router)
app.include_router(issue.router)
app.include_router(github.router)
# Create tables
Base.metadata.create_all(bind=engine)