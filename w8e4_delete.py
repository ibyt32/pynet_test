#!/usr/bin/env python

'''
Python and Ansible for Network Engineers
Week 8, Exercise 4

Remove the two objects created in the previous exercise from the database.
'''

import django
from net_system.models import NetworkDevice


def main():
    '''
    Remove the two objects created in the previous exercise from the database.
    '''
    django.setup()
    try:
        Kelli1 = NetworkDevice.objects.get(device_name='Kelli1')
        Kelli2 = NetworkDevice.objects.get(device_name='Kelli2')
        Kelli1.delete()
        Kelli2.delete()
    except NetworkDevice.DoesNotExist:
        pass
    
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device.device_name, a_device.ip_address

if __name__ == "__main__":
    main()

