import unittest
from astar import *


class TestAStar(unittest.TestCase):

    def test_heuristic(self):
        h_test = h((5, 4), (10, 7))
        h2_test = h((10, 3), (100, 20))

        self.assertEqual(h_test, 8)
        self.assertEqual(h2_test, 107)


if __name__ == '__main__':
    unittest.main()
