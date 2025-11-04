import unittest
from week5.models.Agent import Agent
from week5.models.Location import Location

class TestAgent(unittest.TestCase):
		
    def test_get_location(self):
        loc = Location(3, 4)
        agent = Agent(loc)
        self.assertEqual(agent.get_location(), loc)
        
    def test_set_location(self):
        loc = Location(3, 4)
        agent = Agent(loc)
        loc2 = Location(4, 5)
        agent.set_location()
        self.assertEqual(agent.get_location(), loc2)

    def test_location_attributes(self):
        loc = Location(3, 4)
        agent = Agent(loc)
        self.assertEqual(agent.Location.get_x(), 3)
        self.assertEqual(agent.Location.get_y(), 4)

    def test_location_setters(self):
        loc = Location(3, 4)
        agent = Agent(loc)
        loc2 = Location(4, 5)
        agent.set_location()
        self.assertEqual(agent.get_location(), loc2)

if __name__ == '__main__':
    unittest.main()