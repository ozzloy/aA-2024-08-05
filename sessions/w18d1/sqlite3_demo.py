import sqlite3

DB_FILE = "dev.db"


def print_all_cars():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            "SELECT manu_year, make, model, owner_id FROM cars;"
        )
        cars = curs.fetchall()
        for car in cars:
            print(car)


print_all_cars()
# (1993, 'Mazda', 'Rx7', 1)
# (1995, 'Mitsubishi', 'Eclipse', 2)
# (1994, 'Acura', 'Integra', 3)
