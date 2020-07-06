from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase = "Dylan Buchi"
        result = "Buchi Dylan"
        self.assertEqual(rearrange_name(testcase), result)
        
unittest.main()