from passlib.context import CryptContext
from app.infrastructure.user_repo import create_user
from app.infrastructure.user_repo import get_user_by_email

pwd_context = CryptContext(schemes = ["bcrypt"],deprecated="auto")

def register_user(email:str,password:str):
    existing_user = get_user_by_email(email)
    if existing_user:
        raise ValueError("User already exists")
    hashed_password = pwd_context.hash(password)
    user = create_user(email,hashed_password)
    return user