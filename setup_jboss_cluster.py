from add_users import add_users
from execute_utility_scripts import execute_utility_scripts
from health_check.check_network_connectivity import are_all_machines_reachable
from health_check.copy_asset_files import create_slaves
from health_check.copy_asset_files import process_slave_objects
from start_jboss import start_jboss

import getopt
import sys

def setup_jboss_cluster(argument_list):
    are_all_machines_reachable(argument_list)
    add_users()
    list_of_slave_objects = create_slaves('slaves.properties')
    process_slave_objects(list_of_slave_objects)
    execute_utility_scripts(list_of_slave_objects)
    start_jboss(list_of_slave_objects)
    print "Configuration complete.Please start Master and Slave Nodes.."


def usage():
    print "Usage:python setup-jboss-cluster.py -m=<MasterIP> -s=<CommaSeparatedSlaveIPs"

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv, "m:s:", ["master=", "slaves="])
        setup_jboss_cluster(sys.argv[1:])
    except getopt.GetoptError:
        usage()
        sys.exit()
