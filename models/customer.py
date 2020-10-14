class Customer(): 
    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

    def __repr__(self):
        return f'id: {self.id}, This is {self.name}'
