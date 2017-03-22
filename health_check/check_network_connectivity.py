'''
Created on 26-Jan-2017

@author: abhay
'''

import sys
import subprocess


def are_all_machines_reachable(argument_list):
    # print 'Number of arguments:', len(argument_list)

    if is_master_reachable(argument_list[0]) == True and are_all_slaves_reachable(argument_list[1]) == True:
        print "All machines are connectable"


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
    for ip in ip_list:
        print "Pinging %s" % ip
        if ping(ip) != 0:
            print "Host %s is not reachable.Please check your network connection.Exiting..." % ip
            sys.exit()
    return True


def ping(ip):
    proc = subprocess.Popen(['ping', '-c', '3', ip], stdout=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return proc.returncode


if __name__ == '__main__':
    are_all_machines_reachable(sys.argv)
