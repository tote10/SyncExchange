from fastapi import APIRouter, HTTPException
from app.application.services.user_service import register_user,login_user
from pydantic import BaseModel, EmailStr

router = APIRouter()

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
class RegisterResponse(BaseModel):
    email:EmailStr
    id:int
class LoginRequest(BaseModel):
    email:EmailStr
    password:str
class LoginResponse(BaseModel):
    email:EmailStr
    id:int
@router.post("/register", response_model=RegisterResponse)
def register(data: RegisterRequest):
    try:
        user = register_user(data.email, data.password)
        return RegisterResponse(id=user.id, email=user.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.post("/login", response_model=LoginResponse)
def login(data:LoginRequest):
    try:
        user = login_user(data.email,data.password)
        return LoginResponse(id=user.id,email=user.email)
    except Exception as e:
        raise HTTPException(status_code=401,detail=str(e))