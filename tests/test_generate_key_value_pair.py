from generate_key_value_pair import *
import unittest
import os


class TestGenerateKeyValuePair(unittest.TestCase):
    """Unit test cases for generate_key_value_pair.py"""

    def test_generate_key_value_pair_with_no_input_file(self):
        file = "/home/dumm.properties"
        self.assertRaises(IOError,generate_key_value_pair,file)

    def test_generate_key_value_pair_with_input_file(self):
        filePath = "testAssets/slaves.properties"
        expectedDict = {'192.168.1.4': {'HOST_USER_NAME': 'root', 'PASSWORD': 'Slave@123', 'USER_NAME': 'slaveUserFour', 'HOST_PASSWORD': 'root@123', 'JBOSS_HOME': '/home/jboss_home'}, '192.168.1.3': {'HOST_USER_NAME': 'root', 'PASSWORD': 'Slave@123', 'USER_NAME': 'slaveUserThree', 'HOST_PASSWORD': 'root@123', 'JBOSS_HOME': '/home/jboss_home'}, '192.168.1.2': {'HOST_USER_NAME': 'root', 'PASSWORD': 'Slave@123', 'USER_NAME': 'slaveUserTwo', 'HOST_PASSWORD': 'root@123', 'JBOSS_HOME': '/home/jboss_home'}, '192.168.1.1': {'HOST_USER_NAME': 'root', 'PASSWORD': 'Slave@123', 'USER_NAME': 'slaveUserOne', 'HOST_PASSWORD': 'root@123', 'JBOSS_HOME': '/home/jboss_home'}}
        actualDict = generate_key_value_pair(filePath)
        self.assertEqual(expectedDict,actualDict)


if __name__=="__main__":
    unittest.main()

