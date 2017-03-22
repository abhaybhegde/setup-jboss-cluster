import unittest
from slave import Slave 


class SlaveTest(unittest.TestCase):
    def setUp(self):
        self.slaveObj = Slave('192.168.1.2','/home/jboss_home','userName','passWord','hostUserName','hostPassword')


    def test_get_slave_ip(self):
       #slaveObj = Slave('192.168.1.2','/home/jboss_home','userName','passWord','hostUserName','hostPassword')
       self.assertEquals('192.168.1.2',self.slaveObj.get_slave_ip())

    def test_get_jboss_home(self):
        self.assertEquals('/home/jboss_home', self.slaveObj.get_jboss_home())

    def test_get_user_name(self):
        self.assertEquals('userName',self.slaveObj.get_user_name())

    def test_get_password(self):
        self.assertEquals('passWord',self.slaveObj.get_pass_word())

    def test_get_host_user_name(self):
        self.assertEquals('hostUserName',self.slaveObj.get_host_user_name())

    def test_base64_encode_of_a_password(self):
        self.assertEquals('cGFzc1dvcmQ=',self.slaveObj.get_base64_encode_of_password())

    def test_get_host_pasword(self):
        self.assertEquals('hostPassword',self.slaveObj.get_host_password())
       


if __name__=="__main__":
   unittest.main() 
