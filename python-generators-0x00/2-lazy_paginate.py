from seed import connect_to_db
def paginate_users(page_size, offset=0):
    connection=connect_to_db()
    cursor=connection.cursor(dictionary=True)
    cursor.execute(f"Select * from alx_prodev.user_data limit{page_size} offset {offset}")
    rows=cursor.fetchall()
    for row in rows:
        yield row
