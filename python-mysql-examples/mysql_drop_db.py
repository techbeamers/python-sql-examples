from db_utils import *

def drop_db(db_name="techbeamers"):
    db = connect_db()
    cur = db.cursor()

    # Drop the given database if it exists
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")

    print_separator()
    print(f"Database '{db_name}' dropped")

    db.close()

# Call the above method to drop the database
drop_db()
