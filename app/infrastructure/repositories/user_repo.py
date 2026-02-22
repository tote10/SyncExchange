from app.domain.entities.user import User
from app.infrastructure.database.db import get_connection

def create_user(email:str,password_hash:str)->User:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (email,password_hash) VALUES (%s,%s) RETURNING id, email, password_hash",
        (email,password_hash)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return User(id=row[0], email=row[1], password_hash=row[2])
def get_user_by_email(email:str):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(
        "SELECT id, email, password_hash FROM users WHERE email = %s",
        (email,)
    )
    row=cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if row :
        return User(id=row[0], email=row[1], password_hash=row[2])
    return None