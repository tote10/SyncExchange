from passlib.context import CryptContext
from app.infrastructure.user_repo import create_user
from app.infrastructure.user_repo import get_user_by_email
from pydantic import EmailStr

pwd_context = CryptContext(schemes = ["bcrypt"],deprecated="auto")

def register_user(email:str,password:str):
    existing_user = get_user_by_email(email)
    if existing_user:
        raise ValueError("User already exists")
    if len(password.encode('utf-8')) > 72:
        raise ValueError("Password too long, maximum 72 characters")
    hashed_password = pwd_context.hash(password)
    user = create_user(email,hashed_password)
    return user

def login_user(email:str,password:str):
    user = get_user_by_email(email)
    if not user:
        raise ValueError("User not found")
    if not pwd_context.verify(password,user.hashed_password):
        raise ValueError("Invalid password")
    return user
