from fastapi import FastAPI
from app.presentation.user_api import router as user_router

from app.presentation.user_api import router as login_router

app = FastAPI()
