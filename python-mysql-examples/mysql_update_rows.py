from db_utils import *

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

# Call the function to update data
update_data()
