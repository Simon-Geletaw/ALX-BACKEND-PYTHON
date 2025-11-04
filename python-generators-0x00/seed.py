import mysql.connector
import csv
import uuid
def insert_data(connection,data):
    try:
        cursor = connection.cursor()
        with open(data,'r')as file:
            reader=csv.DictReader(file)
            for row in reader:
                user_id=str(uuid.uuid4())
                name=row['name']
                email=row['email']
                age=int(row['age'])
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))

            connection.commit()
            print("connection commited")
    except Exception as e:
        print(e)
            
def connect_db():
    """Connect to MySQL server (no database yet)"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12131945#Etchelsea',
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection, db_name="ALX_prodev"):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created or already exists")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        cursor.close()

def connect_to_db(db_name="ALX_prodev"):
    """Connect directly to a specific database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12131945#Etchelsea',
            database=db_name,
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            print(f"Connected to database {db_name}")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) NOT NULL,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            PRIMARY KEY (user_id)
        )
        """)
        print("Table 'user_data' created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()
