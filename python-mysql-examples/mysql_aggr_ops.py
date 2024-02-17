from db_utils import *

# Perform SQL Aggregate Functions
def sql_aggr_ops():
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
    print("Avg price in 'products' table:", avg_result)

    # Count
    cur.execute("SELECT COUNT(*) FROM products")
    count_result = cur.fetchone()[0]
    print_separator()
    print("No. of records in 'products' table:", count_result)

# Call the above method to demo mysql aggregate functions
sql_aggr_ops()
