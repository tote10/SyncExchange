from passlib.context import CryptContext
from app.infrastructure.user_repo import create_user
from app.infrastructure.user_repo import get_user_by_email
from pydantic import EmailStr
import re


pwd_context = CryptContext(schemes = ["bcrypt"],deprecated="auto")

def register_user(email:str,password:str):
    existing_user = get_user_by_email(email)
    if existing_user:
        raise ValueError("User already exists")
    if len(password) < 8:
        raise ValueError("Password too short, minimum 8 characters")
    if len(password) > 72:
        raise ValueError("Password too long, maximum 72 characters")
    if not re.search(r"[A-Z]",password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]",password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not re.search(r"[0-9]",password):
        raise ValueError("Password must contain at least one number")
    if not re.search(r"[^A-Za-z0-9]",password):
        raise ValueError("Password must contain at least one special character")
    if " " in password:
        raise ValueError("Password cannot contain spaces")
    if any(ord(c) < 32 for c in password or password.endswith("\\")):
        raise ValueError("Password cannot contain control characters or end with a backslash")
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
