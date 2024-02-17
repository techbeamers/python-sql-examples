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

# Create tables
def create_tables():
    db = connect_db()
    cur = db.cursor()

    # Create 'clients' table
    cur.execute("CREATE TABLE clients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    print_separator()
    print("Table 'clients' created")

    # Create 'orders' table
    cur.execute("CREATE TABLE orders (order_id INT AUTO_INCREMENT PRIMARY KEY, client_id INT, product VARCHAR(255))")
    print_separator()
    print("Table 'orders' created")

    # Create 'products' table
    cur.execute("CREATE TABLE products (product_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2))")
    print_separator()
    print("Table 'products' created")

    db.commit()

# Insert dummy data
def insert_data():
    db = connect_db()
    cur = db.cursor()

    # Insert data into 'clients' table
    sql_clients = "INSERT INTO clients (name, address) VALUES (%s, %s)"
    val_clients = [("Jason Woo", "103 Main St"), ("Alice Johnson", "201 Oak Ave")]

    cur.executemany(sql_clients, val_clients)
    print_separator()
    print("Data inserted into 'clients' table")

    # Insert data into 'orders' table
    sql_orders = "INSERT INTO orders (client_id, product) VALUES (%s, %s)"
    val_orders = [(1, "Laptop"), (2, "Phone"), (1, "Tablet")]

    cur.executemany(sql_orders, val_orders)
    print_separator()
    print("Data inserted into 'orders' table")

    # Insert data into 'products' table
    sql_products = "INSERT INTO products (name, price) VALUES (%s, %s)"
    val_products = [("Laptop", 999.99), ("Phone", 499.99), ("Tablet", 299.99)]

    cur.executemany(sql_products, val_products)
    print_separator()
    print("Data inserted into 'products' table")

    db.commit()

def select_data(tbl_name="clients"):

    db = connect_db()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tbl_name}")
    myresult = cur.fetchall()

    print_separator()
    print(f"Selecting data from {tbl_name}")
    for row in myresult:
        print(row)

# Update data in 'clients' table
def update_data(tbl_name="clients"):
    db = connect_db()
    cur = db.cursor()

    # Update address for the client with ID 1 in the 'clients' table
    sql_update = f"UPDATE {tbl_name} SET address = '456 Oak St' WHERE id = 1"
    cur.execute(sql_update)
    print_separator()
    print(f"Data updated in '{tbl_name}' table")

    db.commit()

# Perform SQL JOIN operation
def sql_join_operation():
    db = connect_db()
    cur = db.cursor()

    # Example of INNER JOIN
    cur.execute("SELECT clients.name, orders.product FROM clients INNER JOIN orders ON clients.id = orders.client_id")

    result = cur.fetchall()

    print_separator()
    print("Results of SQL JOIN operation:")
    for row in result:
        print(row)

# Perform SQL Aggregate Functions
def sql_aggregate_functions():
    db = connect_db()
    cur = db.cursor()

    # Sum
    cur.execute("SELECT SUM(price) FROM products")
    sum_result = cur.fetchone()[0]
    print_separator()
    print("Sum of prices in 'products' table:", sum_result)

    # Average
    cur.execute("SELECT AVG(price) FROM products")
    avg_result = cur.fetchone()[0]
    print_separator()
    print("Average price in 'products' table:", avg_result)

    # Count
    cur.execute("SELECT COUNT(*) FROM products")
    count_result = cur.fetchone()[0]
    print_separator()
    print("Number of records in 'products' table:", count_result)

def drop_table(table_name):
    db = connect_db()
    cur = db.cursor()

    # Drop the specified table if it exists
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")

    print_separator()
    print(f"Table '{table_name}' dropped")

    db.commit()
    db.close()

def drop_database(database_name):
    db = connect_db()
    cur = db.cursor()

    # Drop the specified database if it exists
    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")

    print_separator()
    print(f"Database '{database_name}' dropped")

    db.close()

if __name__ == "__main__":
    create_db()
    create_tables()
    insert_data()
    update_data()
    sql_join_operation()
    sql_aggregate_functions()
    select_data()

    # Uncomment and use the following functions if needed
    drop_table("clients")
    drop_table("orders")
    drop_table("products")

    drop_database("techbeamers")
