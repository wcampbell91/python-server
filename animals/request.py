from models import Animal
from models import Location
from models import Customer
import sqlite3
import json

ANIMALS = [
    Animal(1, 'Jack', 'dog', 'good boy', 1, 2),
    Animal(2, 'Sarah', 'dog', 'good girl', 2, 1),
    Animal(3, 'Jeff', 'cat', 'bad boy', 1, 2),
    Animal(4, 'Stacey', 'cat', 'good girl', 2, 1),
] 


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id 
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            location = Location(row['location_id'],row['location_name'], row['location_address'])

            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'], row['customer_email'],
                                row['customer_password'])

            animal.location = location.__dict__

            animal.customer = customer.__dict__

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)

    # Function with a single parameter
def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'], data['status'],
                        data['location_id'], data['customer_id'])

        return json.dumps(animal.__dict__)

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1].id

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    new_animal = Animal(animal["id"], animal["name"], animal["species"], animal["status"], animal["location_id"], animal["customer_id"])
    ANIMALS.append(new_animal)

    # Return the dictionary with `id` property added
    return new_animal

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you 
    # can access the index value at each item
    for index, animal in enumerate(ANIMALS):
        if animal.id == id:
            # Found the animal. Store the current index.
            animal_index = index

    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                customer_id = ?,
                location_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'], new_animal['status'],
                new_animal['customer_id'], new_animal['location_id'], id))
        
        # Were any rows affected?
        # Did the client send an 'id' that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def get_animal_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row433
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.location_id = ?
        """, (location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['id'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)
        
    return json.dumps(animals)

def get_animals_by_status(status):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

def delete_animal(id):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))
