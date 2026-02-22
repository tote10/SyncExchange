import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.infrastructure.database.db import get_connection

try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    print(f"Database connection successful: {result[0]}")
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error connecting to database: {e}")
