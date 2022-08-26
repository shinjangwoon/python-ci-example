import unittest

from main import hello


class MainTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello world!")


if __name__ == "__main__":
    unittest.main()
