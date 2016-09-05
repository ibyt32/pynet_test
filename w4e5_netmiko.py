#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 5

Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko
to verify your state (i.e. that you are currently in configuration mode).
'''

from netmiko import ConnectHandler
from getpass import getpass


password = getpass()


pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
    }

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    }

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.106.247.76',
    'username': 'pyclass',
    'password': password,
    }


def main():
    '''
    Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko
    to verify your state (i.e. that you are currently in configuration mode).
    '''

    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr2.config_mode()
    output = pynet_rtr2.check_config_mode()
    print
    print 'Checking to see if we are in config mode:'
    print output
    print


if __name__ == "__main__":
    main()

