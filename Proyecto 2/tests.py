import unittest
from RubikCube import Cuboid, Row, RubikCube


class TestRubikCube(unittest.TestCase):
    def setUp(self):
        self.cube = RubikCube()

    def test_initialization(self):
        expected_upper = [0, 1, 2, 3]
        expected_lower = [4, 5, 6, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)

    def test_rotate_left(self):
        self.cube.rotate_left('upper')
        expected_upper = [1, 2, 3, 0]
        expected_lower = [4, 5, 6, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)

    def test_rotate_right(self):
        self.cube.rotate_right('upper')
        expected_upper = [3, 0, 1, 2]
        expected_lower = [4, 5, 6, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)

    def test_rotate_down_front(self):
        self.cube.rotate_down('front')
        expected_upper = [1, 5, 2, 3]
        expected_lower = [0, 4, 6, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)

    def test_rotate_up_front(self):
        self.cube.rotate_up('front')
        expected_upper = [4, 0, 2, 3]
        expected_lower = [5, 1, 6, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)

    def test_rotate_front_right(self):
        self.cube.rotate_front('right')
        expected_upper = [0, 2, 6, 3]
        expected_lower = [4, 1, 5, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)

    def test_rotate_back_right(self):
        self.cube.rotate_back('right')
        expected_upper = [0, 5, 1, 3]
        expected_lower = [4, 6, 2, 7]
        self.assertEqual(
            [c.number for c in self.cube.upper.content], expected_upper)
        self.assertEqual(
            [c.number for c in self.cube.lower.content], expected_lower)


if __name__ == '__main__':
    unittest.main()
