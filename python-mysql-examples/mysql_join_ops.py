from db_utils import *

# Perform SQL JOIN operation
def sql_join_ops():
    db = connect_db()
    cur = db.cursor()

    # Example of INNER JOIN
    cur.execute("SELECT clients.name, orders.product FROM clients INNER JOIN orders ON clients.id = orders.client_id")

    result = cur.fetchall()

    print_separator()
    print("Results of SQL JOIN operation:")
    for row in result:
        print(row)

# Call the function to update data
sql_join_ops()
