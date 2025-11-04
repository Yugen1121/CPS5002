import random
from models.Plakton import Plankton
from models.Shardine import Shardine
from models.Shark import Shark
class Main():
    def __init__(self):
        self.State = [[0 for i in range(20)] for i in range(20)]
        self.Time = 0
        self.initialiseObjects()
    
    def initialiseObjects(self):
        # initialise plankton
        for i in range(random.randint(12, 16)):
            while True:
                x = random.randint(0,20)
                y = random.randint(0,20)
                if self.State[x][y] == 0:
                    self.State[x][y] = Plankton()
                    break
        # initialise Shardine
        for i in range(random.randint(6,8)):
            while True:
                x = random.randint(0,20)
                y = random.randint(0,20)
                if self.State[x][y] == 0:
                    self.State[x][y] = Shardine()
                    break
        # initialise Shark
        for i in range(random.randint(2, 5)):
            while True:
                x = random.randint(0,20)
                y = random.randint(0,20)
                if self.State[x][y] == 0:
                    self.State[x][y] = Shark()
                    break


