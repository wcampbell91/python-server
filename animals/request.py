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
    # Open a connection to the rowbase
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

        # Convert rows of row into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of row returned from rowbase
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
        WHERE a.id = ?
        """, (id, ))

        # Convert rows of row into a Python list
        data = db_cursor.fetchone()

        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        location = Location(data['location_id'],data['location_name'], data['location_address'])

        customer = Customer(data['customer_id'], data['customer_name'], data['customer_address'], data['customer_email'],
                            data['customer_password'])

        animal.location = location.__dict__

        animal.customer = customer.__dict__

        return json.dumps(animal.__dict__)

def create_animal(new_animal):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            (?, ?, ?, ?, ?)
        """, (new_animal['name'], new_animal['breed'], 
                new_animal['treatment'], new_animal['locationId'], 
                new_animal['customerId'], ))
        
        # The `lastrowdi` property on curosr will return 
        # the primary key of the last thing that got added to
        # the rowbase.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the 
        # primary key in the response.
        new_animal['id'] = id

    return json.dumps(new_animal)

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
