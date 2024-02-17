import subprocess

def run_script(script_name):
    print(f"Running script: {script_name}")
    subprocess.run(["python3", script_name])

if __name__ == "__main__":
    scripts = [
        "mysql_create_db.py",
        "mysql_create_table.py",
        "mysql_insert_rows.py",
        "mysql_select_rows.py",
        "mysql_update_rows.py",
        "mysql_join_ops.py",
        "mysql_aggr_ops.py",
        "mysql_drop_table.py",
        "mysql_drop_db.py"
    ]

    for script in scripts:
        run_script(script)

    print("All scripts have been executed.")

