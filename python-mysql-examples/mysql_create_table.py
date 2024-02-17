from db_utils import *

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

# Call the function create the tables
create_tables()
