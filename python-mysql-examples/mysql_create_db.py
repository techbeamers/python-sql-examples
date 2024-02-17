from db_utils import *

def create_db(db_name="techbeamers"):

    db = connect_db("")

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Create the database if it doesn't exist
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    # Close the cursor
    db.close()
    print_separator()
    print(f"Database created as {db_name}")

# Call the function create the database
create_db()
