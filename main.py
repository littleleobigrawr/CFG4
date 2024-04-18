import mysql.connector
from config import USER, PASSWORD, HOST


# Custom exception class for database connection errors
class DdbConnectionError(Exception):
    pass


# Function to connect to the database
def _connect_to_the_database(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# Function to retrieve all data from the database
def get_all():
    try:
        # Define the database name
        db_name = 'fashion_designers'
        # Connect to the database
        db_connection = _connect_to_the_database(db_name)
        # Create a cursor object to execute SQL queries
        cur = db_connection.cursor()
        # Print a message indicating successful database connection
        print("Connected to DB: %s" % db_name)

        # Execute a SQL query to retrieve data about fashion designers
        query = """SELECT designer_name, birth_date FROM designer"""
        cur.execute(query)
        # Fetch all results
        result = cur.fetchall()

        # Execute a SQL query to retrieve data about fashion collections
        query = """SELECT * FROM collection"""
        cur.execute(query)
        # Fetch all results
        result = cur.fetchall()

        # Print the fetched results
        for i in result:
            print(i)
        # Close the cursor
        cur.close()

    # Catch any exception that occurs during database operations
    except Exception:
        # Raise a custom exception to indicate a database connection error
        raise DdbConnectionError("FAILED")

    # Perform cleanup operations even if an exception occurs
    finally:
        # Check if the database connection is open
        if db_connection:
            # Close the database connection
            db_connection.close()
            # Print a message indicating that the connection is closed
            print("Connection closed")


# Function to print fashion data and a closing message
def get_fashion_designer_date():
    # Print a welcome message
    print("Below is the fashion data that you have requested")
    # Call the get_all function to retrieve and print fashion data
    get_all()
    # Print a closing message
    print("I hope you have learnt a lot about fashion today")


# Call the function to print fashion data and closing message
get_fashion_designer_date()
