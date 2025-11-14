import sqlite3
from 0-databaseconnection import DatabaseConnection
class ExecuteQuery(DatabaseConnection):
    def __init__(self,age):
        self.query='SELECT * From users where age > ?'
        self.age=age
    def __enter__(self):
        with DatabaseConnection('users.db') as conn:
            self.cursor=conn.cursor()
            self.cursor.execute(self.query,(self.age,))
            self.results=self.cursor.fetchall()
            return self.results
    def __exit__(self,exc_type,exc_value,traceback):
        print("The cursor is closed properly")
with ExecuteQuery(100) as age_query:
    print(age_query)
    
                     