import unittest
from even_odd import sample


class MyTestCase(unittest.TestCase):
    def test_something(self):
        value = [4, 5, 8, 8, 8, 2, 9]
        output = [0, 1, 0, 0, 0, 0, 1]

        self.assertEqual(output, sample(value))


if __name__ == '__main__':
    unittest.main()
