from models import Customer
import sqlite3
import json

customers = [
    Customer(1, 'Bobo', "123 bunbun ave", "bobo@gmail.com", "buns"),
    Customer(2, 'Frodo', "345 hobo house", "Frodo@gmail.com", "ring"),
    Customer(3, 'Jen', "567 freed ln", "jen@gmail.com", "jin"),
]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        # Just use these. It's a black box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Pytho list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            # Create a customer instance from current row
            # Not ehat the database fields are specified in 
            # exact order of the parameters defined in the 
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'],
                                row['email'], row['password'])

            customers.append(customer.__dict__)

    # use 'json' package to properly serialize list as JSON
    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result in memory
        data = db_cursor.fetchone()

        # Create a customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'], data['email'],
                            data['password'])
    
    return json.dumps(customer.__dict__)

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = customers[-1].id

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    new_customer = Customer(customer["id"], customer["name"], customer["location_id"])
    customers.append(new_customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customers list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(customers):
        if customer.id == id:
            # Found the customer. store the current index
            customer_index = index

    if customer_index >= 0:
        customers.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the customers list, but use enumerate so that
    # you can access teh index value of each item.
    for index, customer in enumerate(customers):
        if customer.id == id:
            # Found the customer. Update teh value.
            customers[index] = Customer(id, new_customer["name"], new_customer["location_id"])
            break

def get_customers_by_email(email):
    with sqlite3.connect("./kennel.db") as conn:        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Wrtie the SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'], 
                                row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
