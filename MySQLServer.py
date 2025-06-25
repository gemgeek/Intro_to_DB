# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    """
    Connects to the MySQL server and creates the 'alx_book_store' database
    if it does not already exist.
    Handles connection errors and ensures the database connection is closed.
    """
    cnx = None  # Initialize connection object to None
    cursor = None # Initialize cursor object to None

    try:
        # Establish a connection to the MySQL server
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="DoyouknowGbeve$25"         
            # port=3306        
        )

        # Create a cursor object, which allows you to execute SQL queries
        cursor = cnx.cursor()

        # SQL command to create the database IF NOT EXISTS
        DB_NAME = 'alx_book_store'
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

        print(f"Attempting to create database '{DB_NAME}'...")
        cursor.execute(create_db_query)

        # Print the success message as required by the assignment
        print(f"Database '{DB_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Handle specific MySQL connector errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your MySQL username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            # This specific error usually means the database doesn't exist,
            # but for CREATE DATABASE, it's more about connection issues if it fails here.
            print(f"Error: Database does not exist. This shouldn't happen during creation.")
        else:
            print(f"Error connecting or creating database: {err}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the cursor and connection are closed, regardless of success or error
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if cnx and cnx.is_connected():
            cnx.close()
            print("MySQL connection closed.")

# Call the function to execute the database creation process
if __name__ == "__main__":
    create_database()
