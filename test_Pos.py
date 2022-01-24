import unittest
from astar import *


class TestPosition(unittest.TestCase):

    def test_clickedPos(self):
        pos_test = get_clicked_pos((203, 101), 200, 800)

        self.assertEqual(pos_test, (50, 25))


if __name__ == '__main__':
    unittest.main()