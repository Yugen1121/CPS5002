import random

class Shark():
    def __init__(self):
        # Lifespan between 12-15 years
        # Energy level 20
        # Sensing level 6-8 blocks
        # Primary shardins 
        # hunger level
        self.life = random.randint(12, 16)
        self.energy = 20
        self.Sense = random.randint(6, 9)
        self.food = "Shardins"
        self.state = self.checkState()
        self.hunger = 1
    # check state
    def checkState(self):
        pass
    # Look for shardins

    # take a random path

    # reproduce

    # eat
