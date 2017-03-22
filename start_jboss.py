import sys
import os
import paramiko
import subprocess

from health_check.copy_asset_files import get_all_slaves_ip_as_a_list
from health_check.copy_asset_files import copy_utility_scripts
from health_check.copy_asset_files import create_ssh_client
from add_users import get_master_attributes


def start_jboss(list_of_slave_objects):
    create_domain_properties_file_for_slaves(list_of_slave_objects)
    create_domain_properties_file_for_master()
    print "Created domain_master.properties to be used by master!"
    print "Created domain.properties to be used by slave nodes!"
#    start_master()
#    start_slaves(list_of_slave_objects)

    
def create_domain_properties_file_for_slaves(list_of_slave_objects):
    #Need to optimize this block
    for  slaves in list_of_slave_objects:
        destinationIp = slaves.get_slave_ip()
        destinationFolder  = slaves.get_jboss_home()
        file = open('domain.properties','w')
        file.write('jboss.bind.address.management={0}\n'.format(destinationIp))
        file.write('jboss.bind.address={0}\n'.format(destinationIp))
        file.write('jboss.domain.master.address={0}'.format(sys.argv[1].split('=')[1]))
        file.close()
        #lot of copy stuff is taking place, can abstract it out
        copy_files(destinationIp,destinationFolder,'domain.properties',slaves)
            
def create_domain_properties_file_for_master():
    masterIp = sys.argv[1].split('=')[1]
    file = open('domain_master.properties','w')
    file.write('jboss.bind.address.management={0}\n'.format(masterIp))
    file.write('jboss.bind.address={0}\n'.format(masterIp))
    file.write('jboss.domain.master.address={0}\n'.format(masterIp))
    file.close()
    masterAttributes = get_master_attributes()
    jbossHome = masterAttributes['JBOSS_HOME']
    subprocess.call('cp domain_master.properties {0}'.format(jbossHome),shell=True)


def start_master():
    currentDir = os.getcwd()
    masterAttributes = get_master_attributes()
    jbossHome = masterAttributes['JBOSS_HOME']
    os.chdir('{0}'.format(jbossHome))
    print "Starting Master Node..."
    subprocess.call('./bin/domain.sh --domain-config=domain.xml --host-config=host.xml -P domain_master.properties &',shell=True)
    os.chdir('{0}'.format(currentDir))

def start_slaves(list_of_slave_objects):
    for slaves in list_of_slave_objects:
        slaveIp = slaves.get_slave_ip()
        slaveJbossHome = slaves.get_jboss_home()
        print "Starting slave:{0}".format(slaveIp)

        
        
def copy_files(targetIp,targetLocation,fileName,slave):
    source = os.getcwd()+'/'+fileName
    hostUserName = slave.get_host_user_name()
    hostPassword = slave.get_host_password()
    ssh = create_ssh_client(targetIp,hostUserName,hostPassword)
    print "Copying file {0} to {1}".format(fileName,targetIp)
    sftp = ssh.open_sftp()
    sftp.put(source, targetLocation+'/domain.properties')
    sftp.close()
    print "Success"
    return

if __name__ == '__main__':
    pass
