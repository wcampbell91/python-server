class Employee():
    def __init__(self, id, name, manager, full_time, hourly_rate):
        self.id = id
        self.name = name
        self.manager = manager
        self.full_time = full_time
        self.hourly_rate = hourly_rate
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, manager: {self.manager}, full_time: {self.full_time}, hourly_rate: {self.hourly_rate}"
