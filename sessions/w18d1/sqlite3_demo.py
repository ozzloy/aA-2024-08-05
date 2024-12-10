import sqlite3

DB_FILE = "dev.db"

with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute("SELECT 'Hello World!'")
    result = curs.fetchone()
    print(result)  # ('Hello World!',)
with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute("SELECT manu_year, make, model FROM cars;")
    cars = curs.fetchall()
    for car in cars:
        print(car)
        # (1993, 'Mazda', 'Rx7')
        # (1995, 'Mitsubishi', 'Eclipse')
        # (1994, 'Acura', 'Integra')
