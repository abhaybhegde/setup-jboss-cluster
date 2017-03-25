'''
Created on 26-Jan-2017

@author: abhay
'''

import subprocess
import sys


def are_all_machines_reachable(argument_list):
    if not argument_list:
        print "Arguments given is empty."
        raise ValueError
    if is_master_reachable(argument_list[0]) == True and are_all_slaves_reachable(argument_list[1]) == True:
        print "All machines are connectable"
    else:
        #One or more machines are not reachable. Hence quit the application
        sys.exit()



def are_all_slaves_reachable(argument_list):
    ip_list = get_all_slaves_ip_as_a_list(argument_list[1:])
    return are_all_ips_reachable(ip_list)


def get_all_slaves_ip_as_a_list(slaves_list):
    slave_ip_list = slaves_list[0:]
    slave_ips = slave_ip_list.split("=")
    ip_string = ''.join(slave_ips[1:])
    list_of_slave_ips = ip_string.split(",")
    print "List of slave ips:%s" % list_of_slave_ips
    return list_of_slave_ips


def is_master_reachable(master_ip):
    ips_list = get_master_ip(master_ip)
    print "Master IP:{0}".format(ips_list)
    return are_all_ips_reachable(ips_list)


def get_master_ip(master_ip):
    ip = master_ip
    list_of_ips = ip.split("=")
    return list_of_ips[1:]


def are_all_ips_reachable(ip_list):
    if not ip_list:
        raise ValueError
    for ip in ip_list:
        print "Pinging %s" % ip
        returnCode = ping(ip) 
#            print "Host %s is not reachable.Please check your network connection.Exiting..." % ip
#            sys.exit()
#        else:
#            return True
        if returnCode == 0:
           continue 
        elif returnCode == 1:
            print "Host %s is not reachable.Please check your network connection.Exiting..." % ip
            return False
    return True 


def ping(ip):
    proc = subprocess.Popen(['ping', '-c', '3', ip], stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return proc.returncode


if __name__ == '__main__':
    # To test at a module level
    # Run from command line as below
    #python check_network_connectivity.py -m=<IP1> -s=<IP2>,<IP3>
    #IP1 could be master IP , IP2,IP3 are slave Ips
    are_all_machines_reachable(sys.argv[1:])
