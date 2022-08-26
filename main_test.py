import unittest

from main import hello


class MainTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello World!")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
    # python -m unittest discover -p "*.test.py"
    # coverage run --source=./ -m unittest discover -p "*.test.py"
    # coverage xml
