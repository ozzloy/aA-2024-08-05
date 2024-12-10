import sqlite3

DB_FILE = "dev.db"


with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute("SELECT 'Hello World!'")
    result = curs.fetchone()
    print(result)  # ('Hello World!',)
