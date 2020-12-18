import unittest

from core.section13.exercise_10 import parse_city


class TestCity(unittest.TestCase):
    def test_parser(self):
        actual = parse_city('Abreu e Lima 100346')
        expected = 'Abreu e Lima', 100346
        self.assertEqual(actual, expected)

        actual = parse_city('NYC 839900')
        expected = 'NYC', 839900
        self.assertEqual(actual, expected)

        actual = parse_city('Bad city 123abc')
        expected = 'Bad city', 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
