from seed import connect_to_db
def paginate_users(page_size, offset):
    connection=connect_to_db()
    cursor=connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows=cursor.fetchall()
    for row in rows:
        yield row
