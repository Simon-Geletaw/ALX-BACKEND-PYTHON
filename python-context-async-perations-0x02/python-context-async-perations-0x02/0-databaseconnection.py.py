import sqlite3
class DatabaseConnection :
    def __init__(self,dbname):
        self.db_name=dbname
        self
        
    def __enter__(self):
        print("Connecting to db.....")
        conn=sqlite3.connect(self.db_name)
        self.connection=conn
        return self.connection
    def __exit__(self,exc_type,exc_value,traceback):
        self.connection.close()
        print("excc",exc_type)
        print("execcc",exc_value)
        print("Connection is closed")
with DatabaseConnection('users.db') as conn:
    cursor=conn.cursor()
    cursor.execute("select * from users ")
    results= cursor.fetchall()
    for result in results :
        print(result)
    cursor.close()