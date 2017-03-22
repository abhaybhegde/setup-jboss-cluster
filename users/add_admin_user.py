'''
Created on 15-Jan-2017

@author: abhay
'''


import os
import subprocess


print("Frim simplePrint.py")


JBOSS_BIN_HOME = '/home/abhay/jboss-domain/master/bin'


def add_admin_user():
    os.chdir(JBOSS_BIN_HOME)
    subprocess.call('ls')
    print("Adding admin user with username as admin and password as Admin@123")
    subprocess.call('./add-user.sh admin Admin@123', shell=True)


if __name__ == '__main__':
    add_admin_user()
