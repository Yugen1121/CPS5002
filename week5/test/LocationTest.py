import unittest
from week5.models.Location import Location

class TestLocation(unittest.TestCase):
    def test_init(self):
        loc = Location(3, 4)
        self.assertEqual(loc.get_x(), 3)
        self.assertEqual(loc.get_y(), 4)

    def test_setters(self):
        loc = Location(3, 4)
        loc.set_x(4)
        loc.set_5(5)
        self.assertEqual(loc.get_x(), 4)
        self.assertEqual(loc.get_y(), 5)

    def test_equals(self):
        loc = Location(3, 4)
        loc2 = Location(3, 4)
        loc3 = Location(2, 2)
        self.assertEqual(loc.equals(loc2), True)
        self.assertEqual(loc.equals(loc3), False)

    def test_str(self):
        loc = Location(3, 4)
        self.assertEqual(str(loc), "X: 3, Y: 4")

if __name__ == '__main__':
    unittest.main()