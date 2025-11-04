from seed import connect_to_db
import mysql.connector

def stream_users_in_batches(batch_size=10):
    """
    Generator that fetches rows from user_data in batches
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")  # must include "FROM user_data"

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        for row in rows:
            yield row  # yield each row to the caller

    cursor.close()
    connection.close()


def batch_processing():
    """
    Process each batch, printing users over age 25
    """
    count = 0
    for row in stream_users_in_batches():
        user_id, name, email, age = row
        if age > 25:
            print("This user is above 25:")
            print(row)
            count += 1
    print(f"Total users above 25: {count}")


# Execute batch processing
batch_processing()
