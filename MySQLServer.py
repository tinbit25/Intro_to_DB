import mysql.connector
from mysql.connector import Error

db_name = "alxbook_store"  # Ensure the name matches exactly as required

try:
    print("Connecting to MySQL server...")  

    # Establishing connection to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="a1b2c3d4e5f6"  # Your MySQL password
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Server!")  
        cursor = connection.cursor()

        # Creating the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"🎉 Database '{db_name}' created successfully!")

except Error as e:
    print(f"❌ Error: {e}")  # Exception handling for MySQL connection errors

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection closed.")
