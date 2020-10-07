employees = [
    {
        "id": 1,
        "name": "Billy",
    },
    {
        "id": 2,
        "name": "Taylor",
    },
    {
        "id": 3,
        "name": "Shane",
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
