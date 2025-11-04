from seed import connect_db
import mysql.connector
def stream_users():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alx_prodev.user_data  limit 6;")

    for row in cursor:
        yield row
    cursor.close()
    connection.close()
rows = stream_users()
for row in rows:
    print(row)
