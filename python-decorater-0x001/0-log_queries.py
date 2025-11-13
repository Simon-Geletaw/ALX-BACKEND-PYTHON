import sqlite3
import functools
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    print("connected successfully") 
    cursor=conn.cursor()
    cursor.execute(query)
    results=cursor.fetchall()
    conn.close()
    return results
users=fetch_all_users(query='SELECT * FROM users')
print(users)