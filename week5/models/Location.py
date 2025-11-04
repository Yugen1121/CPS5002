class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y  

    def equals(self, Location) -> bool:
        x = Location.get_x()
        y = Location.get_y()
        return (self.x == x and self.y == y)
            
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"