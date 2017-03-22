'''
Created on 29-Jan-2017

@author: abhay
'''

import base64


class Slave(object):
    '''
    classdocs
    '''

    def __init__(self, slave_ip, jboss_home, user_name, pass_word, host_user_name, host_password):
        '''
        Constructor
        '''
        self.ip = slave_ip
        self.jboss_home = jboss_home
        self.user_name = user_name
        self.pass_word = pass_word
        self.host_user_name = host_user_name
        self.host_password = host_password

    def get_slave_ip(self):
        return self.ip

    def get_jboss_home(self):
        return self.jboss_home

    def get_user_name(self):
        return self.user_name

    def get_pass_word(self):
        return self.pass_word

    def get_base64_encode_of_password(self):
        base64encoded = base64.b64encode(self.pass_word)
        return base64encoded

    def get_host_user_name(self):
        return self.host_user_name

    def get_host_password(self):
        return self.host_password



