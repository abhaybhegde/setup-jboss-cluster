import subprocess
import os
import paramiko

from health_check.copy_asset_files import create_ssh_client



def execute_utility_scripts(list_of_slave_objects):
        currentDir = os.getcwd()
        for slave in list_of_slave_objects:
            slaveIp = slave.get_slave_ip()
            slaveJbossHome = slave.get_jboss_home()
            hostUserName = slave.get_host_user_name()
            hostPassword = slave.get_host_password()
            print "Executing utility script in slave {0} in folder {1}".format(slaveIp,slaveJbossHome)
            ssh = create_ssh_client(slaveIp,hostUserName,hostPassword)
            stdin, stdout, stderr = ssh.exec_command("cd {0};python utilityScript.py".format(slaveJbossHome))
            print(stdout.read())
            print (stderr.read())
            ssh.close()
        os.chdir(currentDir)
        return

if __name__=="__main__":
    pass
