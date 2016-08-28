#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 2, Exercise 4

Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2)
and prints out both the MIB2 sysName and sysDescr.
'''

from snmp_helper import snmp_get_oid, snmp_extract


COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IPS = ('184.105.247.70', '184.105.247.71')
SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_DESCR = '1.3.6.1.2.1.1.1.0'

def main():
    '''
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2)
    and prints out both the MIB2 sysName and sysDescr.
    '''

    for IP in IPS:
        a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
        print
        for oid in (SYS_NAME, SYS_DESCR):
            snmp_data = snmp_get_oid(a_device, oid)
            output = snmp_extract(snmp_data)
            print output
        print


if __name__ == "__main__":
    main()

