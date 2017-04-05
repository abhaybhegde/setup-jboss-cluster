from xml.dom import minidom
import os


def get_slave_attributes():
    try:
        dict_of_attributes = {}
        with open("slave_attributes.txt") as a_file:
            for a_line in a_file:
                stripped_line = a_line.strip()
                key_value = stripped_line.split("=")
                attribute_name = key_value[0].strip()
                dict_of_attributes[attribute_name] = key_value[1].strip()
        return dict_of_attributes
    except IOError as e:
        print "I/O Error ({0}): {1}".format(e.errno, e.strerror)


def configure_slave_config_files():
    slave_attributes = get_slave_attributes()
    add_slave_attributes(slave_attributes)


def add_slave_user_name(pathToSlaveConfig, slave_user_name):

    doc = minidom.parse(pathToSlaveConfig)
    node_name = doc.getElementsByTagName("host")[0]
    node_name.setAttribute('name', slave_user_name)

    with open(pathToSlaveConfig, 'w') as xmlfile:
        doc.writexml(xmlfile)


def add_slave_attributes(slave_attributes):
    if not slave_attributes:
        raise TypeError
    try:
        slave_user_name = slave_attributes['SLAVE_USER_NAME']
        slave_password = slave_attributes['SLAVE_BAS64_PASSWORD']
        host_slave = os.path.join(
            os.path.dirname(__file__), 'domain/configuration/', 'host-slave.xml')
        add_slave_user_name(host_slave, slave_user_name)
        add_slave_secret_value(host_slave, slave_password)

    except IOError as e:
        print "I/O Error ({0}): {1}".format(e.errno, e.strerror)


def add_slave_secret_value(pathToSlaveConfig, slaveSecretValue):

    doc = minidom.parse(pathToSlaveConfig)
    if (doc.getElementsByTagName('secret')):
        firstChild = doc.getElementsByTagName('secret')
        if firstChild[0].hasAttributes():
            firstChild[0].attributes["value"].value = slaveSecretValue
    with open(pathToSlaveConfig, 'w') as xmlfile:
        doc.writexml(xmlfile)


if __name__ == "__main__":
    configure_slave_config_files()
