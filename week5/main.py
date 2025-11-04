import random
from models.Plakton import Plankton
from models.Shardine import Shardine
from models.Shark import Shark
class Main():
    def __init__(self):
        self.State = [[0 for i in range(20)] for i in range(20)]
        self.IniPlanktonNumber = random.randint(12, 16)
        self.IniShardineNumber = random.randint(6,8)
        self.IniSharkNumber = random.randint(2, 5)
        self.Time = 0
    
    def initialiseObjects(self):
        # initialise plankton
        for i in range(self.IniPlanktonNumber):
            while True:
                x = random.randint(0,20)
                y = random.randint(0,20)
                if self.State[x][y] == 0:
                    self.State[x][y] == Plankton()
                    break
        # initialise Shardine
        for i in range(self.IniShardineNumber):
            while True:
                x = random.randint(0,20)
                y = random.randint(0,20)
                if self.State[x][y] == 0:
                    self.State[x][y] == Shardine()
                    break
        # initialise Shark
        for i in range(self.IniSharkNumber):
            while True:
                x = random.randint(0,20)
                y = random.randint(0,20)
                if self.State[x][y] == 0:
                    self.State[x][y] == Shark()
                    break

    