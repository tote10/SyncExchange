from app.domain.user import User
from app.infrastructure.db import get_connection

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