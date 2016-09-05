#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 8

Use Netmiko to change the logging buffer size (logging buffered <size>)
and to disable console logging (no logging console) from a file on both
pynet-rtr1 and pynet-rtr2.
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
    and to disable console logging (no logging console) from a file on both
    pynet-rtr1 and pynet-rtr2.
    '''

    for device in (pynet1, pynet2):
        device['password'] = password

    for device in (pynet1, pynet2):
        connect_device = ConnectHandler(**device)
        prompt = connect_device.find_prompt()
        connect_device.send_config_from_file('config_file.txt')
        output = connect_device.send_command('show run | inc logg')
        print
        print prompt
        print output


if __name__ == "__main__":
    main()

