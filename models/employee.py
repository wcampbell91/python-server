class Employee():
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, manager: {self.manager}, full_time: {self.full_time}, hourly_rate: {self.hourly_rate}"
