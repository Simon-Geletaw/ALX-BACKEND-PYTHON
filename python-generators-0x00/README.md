#  MySQL CSV Data Importer

A Python script that connects to a MySQL server, creates a database and table (if they don’t exist), and imports user data from a CSV file. Each record is automatically assigned a unique UUID before being inserted into the database.

---

##  Features

- Connects to a MySQL server using `mysql.connector`
- Automatically creates a database (`ALX_prodev`)
- Creates a `user_data` table if not already present
- Reads data from a CSV file
- Inserts data with unique UUIDs
- Handles errors gracefully

