import time
import sqlite3 
import functools
query_cache = {}
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn=sqlite3.connect('users.db')
        cursor=conn.cursor()
        result=func(*args,conn=conn,**kwargs)
        conn.close()
        return result
    return wrapper
        


"""your code goes here"""
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        query_cache[key]=func(*args,**kwargs)
        
        return query_cache
    return wrapper
        
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="select * from users")
print(users)
#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
