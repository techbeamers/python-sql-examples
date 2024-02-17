from db_utils import *

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

# Call the function insert dummy data
insert_data()
