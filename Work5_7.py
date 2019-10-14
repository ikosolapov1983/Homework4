import unittest
from task6_1 import distance

class TestsDistance(unittest.TestCase):
    def testZeroValue(self):
        res = distance(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def testZeroPointAndOnePoint(self):
        res = distance(0, 0, 0, 10)
        self.assertEqual(res, 10)

if __name__ == "__main__":
    unittest.main()
