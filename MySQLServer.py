import mysql.connector
from mysql.connector import Error

db_name = "alx_book_store"

try:
    print("Connecting to MySQL server...")  

    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Use your correct username
        password="a1b2c3d4e5f6"  # Replace with your actual password
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Server!")  
        cursor = connection.cursor()
        
        # Create database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"🎉 Database '{db_name}' created successfully!")

except Error as e:
    print(f"❌ Error: {e}")  # This will now display any connection errors

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection closed.")  
