import unittest
from check_network_connectivity import are_all_machines_reachable
from check_network_connectivity import are_all_ips_reachable

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


if __name__ == "__main__":
    unittest.main()
