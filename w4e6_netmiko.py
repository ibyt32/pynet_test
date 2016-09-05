#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 6

Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2 and
juniper-srx.
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
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2 and
    juniper-srx.
    '''

    for device in (pynet1, pynet2, juniper_srx):
        device['password'] = password

    for device in (pynet1, pynet2, juniper_srx):
        connect_device = ConnectHandler(**device)
        prompt = connect_device.find_prompt()
        output = connect_device.send_command('show arp')
        print
        print prompt
        print output


if __name__ == "__main__":
    main()

