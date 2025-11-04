from seed import connect_to_db
import mysql.connector
count=0
def stream_users_in_batches(batch_size=10):
    connection=connect_to_db()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM alx_prodev.user_data ;")
    while True:
        rows=cursor.fetchmany(batch_size)
        if  not rows:
            break
        print(f" number of fetched{len(rows)}")
        for row in rows:
                 yield
    cursor.close()
    connection.close()
    
def batch_processing():
    count=0
    rows=stream_users_in_batches()
    for row in rows:
        user_id,name,email, age=row
        if age>25:
            print(" this are from above 25")
            yield row
            count=count+1
    print(count)
rows=batch_processing()