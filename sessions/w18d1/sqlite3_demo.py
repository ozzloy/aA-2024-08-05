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


def get_owners_cars(owner_id):
    """
    Fetch and return all cars in the cars table
    :param owner_id: <int> the id of the owner who's cars to return
    :return: <list> the results of the query
    """
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
                     SELECT manu_year, make, model FROM cars
                     WHERE owner_id = :owner_id
                     """,
            {"owner_id": owner_id},
        )
        results = curs.fetchall()
        return results


print(get_owners_cars(1))  # [(1993, 'Mazda', 'Rx7')]

print_all_cars()
# (1993, 'Mazda', 'Rx7', 1)
# (1995, 'Mitsubishi', 'Eclipse', 2)
# (1994, 'Acura', 'Integra', 3)
