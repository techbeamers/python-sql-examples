import mysql.connector

def connect_db(db_name="techbeamers"):

    if db_name == "":
        # Connect to MySQL server without specifying a database
        db = mysql.connector.connect(
           host="127.0.0.1",
           user="temp",
           password="temp"
        )
    else:
        # Reconnect to the specific database
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="temp",
            password="temp",
            database=db_name
        )

    return db

def print_separator():
    print("*" * 50)
