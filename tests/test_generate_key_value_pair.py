from generate_key_value_pair import *
import unittest


class TestGenerateKeyValuePair(unittest.TestCase):
    """Unit test cases for generate_key_value_pair.py"""

    def test_generate_key_value_pair_with_no_input_file(self):
        file = "/home/dumm.properties"
        self.assertRaises(IOError,generate_key_value_pair,file)





if __name__=="__main__":
    unittest.main()

