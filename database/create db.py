import sqlite3

conn = sqlite3.connect("resumes.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
id INTEGER PRIMARY KEY AUTOINCREMENT,
resume_name TEXT,
percentage REAL
)
""")

conn.commit()
conn.close()

print("Database Created")