import sqlite3 
import functools

"""your code goes here"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn=sqlite3.connect('users.db')
        cursor=conn.cursor()
        user_id='5d2b34fa-54fb-49db-b22e-82ff7a8fbb2b'
        return func(*args,conn=conn,**kwargs)

    return wrapper
        
def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn=kwargs.get('conn')
        try:
            result=func(*args, **kwargs)
            conn.commit()
            return result
        except sqlite3.IntegrityError as e:
             print("Integrity error! Rolling back.", e)
             conn.rollback()
        except sqlite3.OperationalError as e:
            print("Operational error! Rolling back.", e)
            conn.rollback()
        except sqlite3.DatabaseError as e:
            print("Database error! Rolling back.", e)
            conn.rollback()
        finally:
            conn.close()
    return wrapper
    
@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')