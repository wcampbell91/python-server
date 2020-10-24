import sqlite3
import json
from models import Employee, Location

employees = []


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM employee a
        JOIN location l
            ON l.id = a.location_id
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'],
            row['location_id'])

            location = Location(row['id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM employee a
        JOIN location l
            ON l.id = a.location_id
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'],
        data['location_id'])

        location = Location(data['id'], data['location_name'], data['location_address'])

        employee.location = location.__dict__

    return json.dumps(employee.__dict__)

def create_employee(employee):
    max_id = employees[-1].id
    new_id = max_id + 1

    employee["id"] = new_id
    
    new_employee = Employee(employee["id"], employee["name"], employee["manager"], employee["full_time"], employee["hourly_rate"])
    employees.append(new_employee)

    return employee

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate over employees list, but use enumerate() so you can 
    # access the index value of each item
    for index, employee in enumerate(employees):
        if employee.id == id:
            # Found the employee. store the current index
            employee_index = index

    if employee_index >= 0:
        employees.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the employees list, but use enumerate() so you
    # can access the index of each item.
    for index, employee in enumerate(employees):
        if employee.id == id:
            # Found the employee. Update the value
            employees[index] = Employee(id, new_employee["name"], new_employee["manager"], new_employee["full_time"], new_employee["hourly_rate"])
            break

def get_employee_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'],
                                row['location_id'])
            employees.append(employee.__dict__)
        
    return json.dumps(employees)
