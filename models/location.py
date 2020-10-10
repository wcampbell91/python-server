class Location():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, address: {self.address}"
