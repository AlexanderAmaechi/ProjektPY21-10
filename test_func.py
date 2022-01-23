import unittest
from astar import *


class TestAstar(unittest.TestCase):

    def test_heuristic(self):
        h_test = h((9, 4), (10, 7))
        h2_test = h((10, 3), (100, 20))

        self.assertEqual(h_test, 4)
        self.assertEqual(h2_test, 107)

    def test_clickedPos(self):
        pos_test = get_clicked_pos((203, 101), 200, 800)

        self.assertEqual(pos_test, (50, 25))


if __name__ == '__main__':
    unittest.main()
