from models.animal import Animal

ANIMALS = [
    Animal(1, 'Jack', 'dog', 'good boy', 1, 2),
    Animal(2, 'Sarah', 'dog', 'good girl', 2, 1),
    Animal(3, 'Jeff', 'cat', 'bad boy', 1, 2),
    Animal(4, 'Stacey', 'cat', 'good girl', 2, 1),
] 


def get_all_animals():
    return ANIMALS

    # Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        if animal.id == id:
            requested_animal = animal

    return requested_animal

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
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal.id == id:
            # Found the animal. Update the value.
            ANIMALS[index] = Animal(id, new_animal["name"], new_animal["species"], new_animal["status"], new_animal["location_id"], new_animal["customer_id"])
            break
