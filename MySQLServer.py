# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    
    cnx = None  
    cursor = None 

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

        
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        
        DB_NAME = 'alx_book_store' # Keeping this for the print statement

        print(f"Attempting to create database '{DB_NAME}'...")
        cursor.execute(create_db_query)

        # Print the success message as required by the assignment
        print(f"Database '{DB_NAME}' created successfully!")

    except mysql.connector.Error as err:
        # Handle specific MySQL connector errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your MySQL username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            # This error occurs if the database does not exist
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
