from Location import Location
class Agent():
    def __init__(self, Location: Location):
        self.Location = Location

    
    def get_location(self) -> Location:
        return self.Location
    
    def set_location(self, new_location: Location) -> None:
        self.Location = new_location 