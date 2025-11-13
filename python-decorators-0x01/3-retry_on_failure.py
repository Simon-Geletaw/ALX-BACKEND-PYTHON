import time
import sqlite3 
import functools

#### paste your with_db_decorator here
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn=sqlite3.connect('users.db')
        cursor=conn.cursor()
        user_id='5d2b34fa-54fb-49db-b22e-82ff7a8fbb2b'
        func(*args,conn=conn,user_id=user_id,**kwargs)
        conn.close()
    return wrapper
""" your code goes here"""
def retry_on_failure(func,retries,delay):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        conn= kwargs.get('conn')
        time.sleep(delay)
        return func(*args, **kwargs)
    return wrapper
        
        
    
    

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)