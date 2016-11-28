#!/usr/bin/env python

'''
Python and Ansible for Network Engineers
Week 8, Exercise 3

Create two new test NetworkDevices in the database. Use both direct object
creation and the .get_or_create() method to create the devices.
'''

import django
from net_system.models import NetworkDevice


def main():
    '''
    Create two new test NetworkDevices in the database. Use both direct object
    creation and the .get_or_create() method to create the devices.
    '''
    django.setup()
    devices = NetworkDevice.objects.all()

    Kelli1 = NetworkDevice(
        device_name='Kelli1',
        device_type='cisco_ios',
        ip_address='10.10.10.10',
        port=22,
    )
    Kelli1.save()

    Kelli2 = NetworkDevice.objects.get_or_create(
        device_name='Kelli2',
        device_type='cisco_ios',
        ip_address='11.11.11.11',
        port=22,
    )
    
    for a_device in devices:
        print a_device.device_name, a_device.ip_address

if __name__ == "__main__":
    main()

