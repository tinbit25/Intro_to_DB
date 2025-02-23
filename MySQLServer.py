import mysql.connector
from mysql.connector import Error

db_name = "alx_book_store"  # Ensure this matches the expected name

try:
    # Connecting to the MySQL server
    print("Connecting to MySQL server...")
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="a1b2c3d4e5f6"  # Replace with your MySQL password
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Server!")  
        cursor = connection.cursor()

        # Execute the exact statement required
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("🎉 Database 'alx_book_store' created successfully!")

except Error as e:
    # Handling connection errors and other exceptions
    print(f"❌ Error: {e}")

finally:
    # Ensuring resources are properly closed
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection closed.")
