from db_utils import *

def select_data(tbl_name="clients"):

    db = connect_db()
    cur = db.cursor()
    cur.execute(f"SELECT * FROM {tbl_name}")
    myresult = cur.fetchall()

    print_separator()
    print(f"Selecting data from {tbl_name}")
    for row in myresult:
        print(row)

# Call the function to fetch records
select_data()
