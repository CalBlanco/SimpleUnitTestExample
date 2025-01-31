import unittest
from example_feature import NamedCoords
import math

class NamedCordTest(unittest.TestCase):
    def setUp(self): #set up is called before each test
        self.p1 = NamedCoords(0,0, 'p1')
        self.p2 = NamedCoords(10,10, 'p2')

    def test_equality(self): #assert that this boolean condition returns true
        self.assertTrue(self.p1 == NamedCoords(0,0, 'arbitrary'), 'Points should equal if their coordinates are the same')
    
    def test_repr(self): #assert that the string representation matches what we want
        self.assertEqual(repr(self.p1), 'Named-Coords: (0, 0) - p1', 'Point should be represented by desired format')

    def test_add(self):
        added = self.p1 + self.p2
        self.assertEqual(added, (10,10), 'Points should add to (10,10)')
    
    def test_sub(self):
        sub = self.p1 - self.p2
        self.assertEqual(sub, (-10,-10), 'Points should subtract to -10, -10')
    
    def test_distance_noerror(self):
        dist = self.p1.calc_distance(self.p2)
        self.assertEqual(dist, math.sqrt(200), 'Distance should be the square root of 200')
    
    def test_distance_error(self):
        far_point = NamedCoords(2000, 2000, 'bad')
        self.assertRaises(Exception, self.p1.calc_distance, far_point)


#run this class by calling `python ./example_features/test.py`
if __name__ == '__main__':
    unittest.main()