from models.employee import Employee
employees = [
    Employee(1, "Billy", True, True, 10),
    Employee(2, "Taylor", True, False, 11),
    Employee(3, "Shane", False, False, 7)
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
        if employee.id == id:
            requested_employee = employee

    return requested_employee

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
