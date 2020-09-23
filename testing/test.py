import sys
import os
import unittest
sys.path.append(os.getcwd())
from testing.add_five import add_five_to


class TestAddFive(unittest.TestCase):
    def test_add_five_to(self):
        test = 10
        result = add_five_to(test)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
