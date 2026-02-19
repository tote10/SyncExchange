from fastapi import FastAPI
from app.presentation.user_api import router as user_router,LoginRequest

app = FastAPI()
app.include_router(user_router)
app.include_router(login_router)