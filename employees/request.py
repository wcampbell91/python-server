employees = [
    {
        "id": 1,
        "name": "Billy",
        "manager": True,
        "full-time": True,
        "hourly-rate": 10,
    },
    {
        "id": 2,
        "name": "Taylor",
        "manager": True,
        "full-time": True,
        "hourly-rate": 11,
    },
    {
        "id": 3,
        "name": "Shane",
        "manager": True,
        "full-time": False,
        "hourly-rate": 10,
    }
]


def get_all_employees():
    return employees

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employees list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in employees:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = employees[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id
    
    employees.append(employee)

    return employee

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate over employees list, but use enumerate() so you can 
    # access the index value of each item
    for index, employee in enumerate(employees):
        if employee["id"] == id:
            # Found the employee. store the current index
            employee_index = index

    if employee_index >= 0:
        employees.pop(employee_index)
