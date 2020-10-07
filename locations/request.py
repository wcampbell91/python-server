locations = [
    {
        "id": 1,
        "city": "New York City",
    },
    {
        "id": 2,
        "city": "Los Angeles",
    },
    {
        "id": 3,
        "city": "Chicago",
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
