import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn=sqlite3.connect('users.db')
        cursor=conn.cursor()
        user_id='5d2b34fa-54fb-49db-b22e-82ff7a8fbb2b'
        func(*args,conn=conn,user_id=user_id,**kwargs)
        conn.close()
    return wrapper
        

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id()
print(user)