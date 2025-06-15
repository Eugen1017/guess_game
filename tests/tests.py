import unittest
from core.logic import get_random_number

class TestRandoms(unittest.TestCase):
    def test_easy_mode(self):
        number = get_random_number(1)
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 9)

    def test_normal_mode(self):
        number = get_random_number(2)
        self.assertGreaterEqual(number, 10)
        self.assertLessEqual(number, 99)

    def test_hard_mode(self):
        number = get_random_number(3)
        self.assertGreaterEqual(number, 100)
        self.assertLessEqual(number, 999)


if __name__ == '__main__':
    unittest.main()