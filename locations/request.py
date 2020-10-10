locations = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
    ]


def get_all_locations():
    return locations

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locations list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in locations:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last animal in the list
    max_id = locations[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an 'id' property to the animal dictionary
    location["id"] = new_id
    
    # Add the location dirctionary to the list
    locations.append(location)

    return location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(locations):
        if location["id"] == id:
            location_index = index
    
    if location_index >= 0:
        locations.pop(location_index)
