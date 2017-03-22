'''
Created on 29-Jan-2017

@author: abhay
'''


import sys
import os

from configure_slaves.slave import Slave
from health_check.check_network_connectivity import get_all_slaves_ip_as_a_list
from health_check.generate_key_value_pair import generate_key_value_pair
import paramiko


list_of_slave_objects = []


def create_slaves(asset_file_path):
    slave_ips = get_all_slaves_ip_as_a_list(sys.argv[2])
    slave_attributes = generate_key_value_pair(asset_file_path)
    for ip in slave_ips:
		print 'Creating Slave {0}'.format(ip)
		list_of_slave_objects.append(Slave(ip, slave_attributes[ip]['JBOSS_HOME'], slave_attributes[
                                     ip]['USER_NAME'], slave_attributes[ip]['PASSWORD'], slave_attributes[ip]['HOST_USER_NAME'], slave_attributes[ip]['HOST_PASSWORD']))

    return list_of_slave_objects


def process_slave_objects(slave_objects):

    for slave in slave_objects:
        destination_ip = slave.get_slave_ip()
        destination_home = slave.get_jboss_home()
        copy_utility_scripts(destination_ip, destination_home, slave)
        copy_slave_attributes(destination_ip, destination_home, slave)


def create_ssh_client(ip,host_user_name,host_password):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=host_user_name, password=host_password)
    return ssh


def copy_utility_scripts(ip, path, slave_obj):
	source = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utilityScript.py'))
	destination = slave_obj.get_jboss_home() + '/' + 'utilityScript.py'
	host_user_name = slave_obj.get_host_user_name()
	host_password  = slave_obj.get_host_password()
	ssh = create_ssh_client(ip, host_user_name, host_password)
	print "Copying utilityScript.py to {0}".format(ip)
	sftp = ssh.open_sftp()
	sftp.put(source, destination)
	sftp.close()
	print "Success!"


def copy_slave_attributes(ip, destinationFolder, slaveObj):
    if not ip:
        raise TypeError
    try:
		f = open("slave_attributes.txt", "w+")
		f.write("SLAVE_USER_NAME={0}\n".format(slaveObj.get_user_name()))
		f.write("SLAVE_BAS64_PASSWORD={0}\n".format(slaveObj.get_base64_encode_of_password()))
		f.close()
		source = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'slave_attributes.txt'))
		destination = slaveObj.get_jboss_home() + '/' + 'slave_attributes.txt'
		host_user_name = slaveObj.get_host_user_name()
		host_password  = slaveObj.get_host_password()
		ssh = create_ssh_client(ip,host_user_name,host_password)
		sftp = ssh.open_sftp()
		sftp.put(source,destination)
		sftp.close()
		print "Copying slave_attributes.txt to {0} sucess!".format(ip)

    except IOError as e:
        print "I/O Error ({0}): {1}".format(e.errno, e.strerror)


if __name__ == "__main__":
    #list_of_slave_objects = create_slaves('../slaves.properties')
    pass

