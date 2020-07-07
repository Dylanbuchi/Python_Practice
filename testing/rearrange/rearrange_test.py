import unittest
from rearrange import rearrange_name


class TestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase = "Dylan Buchi"
        result = "Buchi Dylan"
        self.assertEqual(rearrange_name(testcase), result)

    def test_empty(self):
        testcase = ""
        result = ""
        self.assertEqual(rearrange_name(testcase), result)

    def test_one_name(self):
        testcase = "Dylan"
        result = "Dylan"
        self.assertEqual(rearrange_name(testcase), result)
        

unittest.main()
