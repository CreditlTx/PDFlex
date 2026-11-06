import sqlite3
import os

# Database file path
DB_PATH = os.path.join("data", "documents.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():

    # Create data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Connect to database
    conn = get_connection()
    cursor = conn.cursor()

    # Create document table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS document(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        path TEXT,
        thumbnail_path TEXT,
        tags TEXT,
        description TEXT,
        upload_date TEXT,
        lecture_date TEXT,
        total_pages INTEGER
    )
    """)

    # Save changes
    conn.commit()

    print("Database operation successful")

    # Close connection
    conn.close()
