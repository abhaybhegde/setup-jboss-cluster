'''
Created on 15-Jan-2017

@author: abhay
'''


import os
import subprocess
import base64


JBOSS_BIN_HOME = '/home/abhay/jboss-domain/master/bin'


def add_slave_user():
    os.chdir(JBOSS_BIN_HOME)
    print "Currently in %s" % os.getcwd()
    print "Adding following slave users"
    print ('Slave One: username=%(userName)s,password=%(password)s',
           '% {"userName": "slaveOne", "password": "SlaveOne@123"}')

    subprocess.call(
        './add-user.sh -u slaveOne -p SlaveOne@123 -g mgmtgroup -r ManagementRealm', shell=True)
    base64encoded = base64.b64encode('SlaveOne@123')
    print ('Base64 Encode of the password %(password)s is %(base64Encoded)s',
           ' % {"password": "SlaveOne@123", "base64Encoded": base64encoded}')


if __name__ == '__main__':
    add_slave_user()
