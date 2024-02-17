from db_utils import *

def drop_table(tbl_name="*"):
    db = connect_db()
    cur = db.cursor()

    # Drop the given table if it exists
    cur.execute(f"DROP TABLE IF EXISTS {tbl_name}")

    print_separator()
    print(f"Table '{tbl_name}' dropped")

    db.commit()
    db.close()

# Call the above method to drop the table
# Uncomment and use the following functions if needed
drop_table("clients")
drop_table("orders")
drop_table("products")

