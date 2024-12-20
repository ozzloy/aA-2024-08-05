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


def add_new_car(manu_year, make, model, owner_id):
    """
    Add the given car to the database
    :param manu_year: <int> the year the car was made
    :param make: <string> the manufacturer of the car
    :param model: <string> the model of the car
    :param owner_id: <int> the id number of the owner
    """
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        # curs.execute(f'INSERT INTO {table}{columns} VALUES{values};')
        curs.execute(
            """
                     INSERT INTO cars (manu_year, make, model, owner_id)
                     VALUES (:manu_year, :make, :model, :owner_id)
                     """,
            {
                "manu_year": manu_year,
                "make": make,
                "model": model,
                "owner_id": owner_id,
            },
        )


add_new_car(2000, "Ford", "Lightning", 2)

add_new_car(1994, "Toyota", "Supra", 2)

print_all_cars()
# (1993, 'Mazda', 'Rx7', 1)
# (1995, 'Mitsubishi', 'Eclipse', 2)
# (1994, 'Acura', 'Integra', 3)
# (2000, 'Ford', 'Lightning', 2)
# (1994, 'Toyota', 'Supra', 2)


def change_car_owner(car_id, new_owner_id):
    """
    Update the owner of a car, both by record id
    :param car_id: <int> the id of the car to change
    :param new_owner_id: <int> the owner_id to give ownership to
    """
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
                     UPDATE cars SET owner_id = :new_owner_id
                     WHERE id = :car_id
                     """,
            {"car_id": car_id, "new_owner_id": new_owner_id},
        )


change_car_owner(5, 1)

print_all_cars()


# (1993, 'Mazda', 'Rx7', 1)
# (1995, 'Mitsubishi', 'Eclipse', 2)
# (1994, 'Acura', 'Integra', 3)
# (2000, 'Ford', 'Lightning', 2)
# (1994, 'Toyota', 'Supra', 1)       <- owner_id is now 1
def delete_car(car_id):
    """
    Delete the record for a car given an id for that car
    :param car_id: <int> the id of the car record to remove
    """
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
                     DELETE FROM cars WHERE id = :car_id
                     """,
            {"car_id": car_id},
        )


delete_car(2)

print_all_cars()
# (1993, 'Mazda', 'Rx7', 1)
# (1994, 'Acura', 'Integra', 3)
# (2000, 'Ford', 'Lightning', 2)
# (1994, 'Toyota', 'Supra', 1)
