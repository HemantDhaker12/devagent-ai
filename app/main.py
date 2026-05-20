from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models import user
from app.api.routes import auth, issue

app = FastAPI()

app.include_router(auth.router)
app.include_router(issue.router)
# Create tables
Base.metadata.create_all(bind=engine)