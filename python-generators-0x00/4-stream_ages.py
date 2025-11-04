from seed import connect_to_db
def stream_user_ages(batch_size=10):
    connection=connect_to_db()
    cursor=connection.cursor()
    cursor.execute("SELECT age from  alx_prodev.user_data;")
    while True:
        rows =cursor.fetchmany(batch_size)
        if not rows:
            break
        for row in rows:
            yield float(row[0])
def Calculate_avg_age(rows):
    count=1
    total=0.0
    for age in rows:
        total=total + age 
        count=count+1
    print(str(total/count))
rows=stream_user_ages()
Calculate_avg_age(rows)