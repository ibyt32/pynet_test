#!/usr/bin/env python
'''
Python for Network Engineers Week 7 Exercise 1
Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the
'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields
for each of the interfaces on the switch. Accomplish this using Arista's
pyeapi.
'''

import pyeapi


def main():
    '''
    Use Arista's eAPI to obtain 'show interfaces' from the switch.
    '''
    eapi_conn = pyeapi.connect_to("pynet-sw3")

    interfaces = eapi_conn.enable("show interfaces")

    # Strip off outer list
    interfaces = interfaces[0]
    # Only use result dictionary
    interfaces = interfaces["result"]
    # Go one more step down to the interfaces
    interfaces = interfaces['interfaces']

    # From Kirk's code
    data_stats = {}
    # inOctets/outOctets are fields inside 'interfaceCounters' dict
    for interface, int_values in interfaces.items():
        int_counters = int_values.get('interfaceCounters', {})
        data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

    # Print output data
    print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
    for intf, octets in data_stats.items():
        print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])


if __name__ == '__main__':
    main()

