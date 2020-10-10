class Customer(): 
    def __init__(self, id, name, location_id):
        self.id = id
        self.name = name
        self.location_id = location_id

    def __repr__(self):
        return f'id: {self.id}, This is {self.name} their location ID is {self.location_id}'
