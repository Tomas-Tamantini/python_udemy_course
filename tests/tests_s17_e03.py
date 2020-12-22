import unittest
from core.section17.exercise_3_s17 import Circle


class TestCircle(unittest.TestCase):
    def test_perimeter(self):
        c = Circle(10)
        expected = 62.8318530718
        actual = c.perimeter
        self.assertAlmostEqual(expected, actual, places=5)

    def test_area(self):
        c = Circle(10)
        expected = 314.159265359
        actual = c.area
        self.assertAlmostEqual(expected, actual, places=5)


if __name__ == '__main__':
    unittest.main()
