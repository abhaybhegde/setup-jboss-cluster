import sys
import subprocess
import os

from health_check.generate_key_value_pair import generate_key_value_pair

def add_users():
	add_admin_user()
	add_slave_users()

def add_slave_users():
	slaveAttributes = {}
	slaveAttributes = generate_key_value_pair('slaves.properties')
	#need to optimize
	masterAttributes = get_master_attributes()
	jbossHome = masterAttributes['JBOSS_HOME']
	currentDir = os.getcwd()
	for key,value in slaveAttributes.iteritems():
		slaveUserName = slaveAttributes[key]['USER_NAME']
		slavePassword = slaveAttributes[key]['PASSWORD']
		print "Adding slave user: {0}".format(slaveUserName)
		os.chdir(jbossHome + '/bin')
		subprocess.call('./add-user.sh -s -u {0} -p {1} -g mgmtgroup -r ManagementRealm'.format(slaveUserName,slavePassword), shell=True)
	os.chdir(currentDir)


def add_admin_user():
	masterAttributes = get_master_attributes()
	userName = masterAttributes['ADMIN_USERNAME']
	passWord = masterAttributes['ADMIN_PASSWORD']
	jbossHome = masterAttributes['JBOSS_HOME']
	currentDir = os.getcwd()
	os.chdir(jbossHome + '/bin')
	subprocess.call('./add-user.sh -s {0} {1}'.format(userName,passWord), shell=True)
	print "Adding admin user:{0} success".format(userName)
	os.chdir(currentDir)


def get_master_attributes():
	masterAttributes = {}

	with open('master.properties','rt') as file:
		for line in file:
			 key_value = line.strip().split('=')
			 key = key_value[0].strip()
			 value = key_value[1].strip()
			 masterAttributes[key] = value
			
	return masterAttributes
	






if __name__=="__main__":
	add_users()
