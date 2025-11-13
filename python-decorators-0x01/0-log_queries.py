import sqlite3
import functools
import logging
import csv
import uuid
from datetime import datetime

# --- Decorator ---
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Finished: {func.__name__}")
        return result
    return wrapper


# --- Fetch data from SQLite ---
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    print("Connected successfully") 
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def inser_data():
    con=sqlite3.connect('users.db')
    cursor=con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
            user_id CHAR(36) NOT NULL,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            PRIMARY KEY (user_id));
     """)
    print("Successfully created")
def insert_data(data):
    connection=sqlite3.connect('users.db')
    try:
        cursor = connection.cursor()
        with open(data,'r')as file:
            reader=csv.DictReader(file)
            for row in reader:
                user_id=str(uuid.uuid4())
                name=row['name']
                email=row['email']
                age=int(row['age'])
                cursor.execute("""
                    INSERT INTO users(user_id, name, email, age)
                    VALUES (?, ?, ?, ?)
                """, (user_id, name, email, age))

            connection.commit()
            print("connection commited")
    except Exception as e:
        print(e)
results=fetch_all_users('select * from users')