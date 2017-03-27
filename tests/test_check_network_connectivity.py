from check_network_connectivity import *
import unittest

class TestNetworkConnectivity(unittest.TestCase):
    """Unit test cases for $SCRIPTS_ROOT/health_check/check_network_connectivity.py"""

    #@unittest.skip
    def test_are_all_machines_reachable_with_empty_arguments(self):
        argumentList = []
        self.assertRaises(ValueError,are_all_machines_reachable,argumentList)

    def test_are_all_ips_reachable_for_empty_input(self):
        argumentList = []
        self.assertRaises(ValueError,are_all_ips_reachable,argumentList)

    def test_are_all_ips_reachable_with_non_reachable_ips(self):
        argumentList = ['10.168.1.7']
        result =  are_all_ips_reachable(argumentList)
        self.assertEqual(False,result)

    def test_get_master_ip(self):
        masterIp = "-m=192.169.1.1"
        result = get_master_ip(masterIp)
        expected = ['192.169.1.1']
        self.assertEqual(result,expected)

    def test_get_master_ip_for_empty_input(self):
        masterIp = None;
        self.assertRaises(ValueError,get_master_ip,masterIp)

    def test_is_master_reachable_for_empty_input(self):
        masterIp = None
        self.assertRaises(ValueError,is_master_reachable,masterIp)

    def test_is_master_reachable_for_non_reachable_ip(self):
        masterIp = "-m=10.10.10.1"
        self.assertFalse(is_master_reachable(masterIp))

if __name__ == "__main__":
    unittest.main()
