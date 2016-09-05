#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 7

Use Netmiko to change the logging buffer size (logging buffered <size>)
on pynet-rtr2.
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
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
    }


def main():
    '''
    Use Netmiko to change the logging buffer size (logging buffered <size>)
    on pynet-rtr2.
    '''

    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr2.config_mode()
    config_commands = ['logging buffered 102400']
    output = pynet_rtr2.send_config_set(config_commands)
    print
    print output
    print


if __name__ == "__main__":
    main()

