import mysql.connector
from mysql.connector import Error

db_name = "alxbookstore"  # Updated to match the exact name as per the requirement

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

        # Create the database if it doesn't already exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"🎉 Database '{db_name}' created successfully!")

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
