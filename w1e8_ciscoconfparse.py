#!/usr/bin/env python

# Python and Ansible for Network Engineers
# Week 1, Exercise 8
#
# Write a Python program using ciscoconfparse that parses cisco_ipsec.txt.
# Note, this config file is not fully valid (i.e. parts of the configuration
# are missing). The script should find all of the crypto map entries in the
# file (lines that begin with 'crypto map CRYPTO') and for each crypto map
# entry print out its children.

from ciscoconfparse import CiscoConfParse


def main():
    '''
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the children of each crypto map.
    '''
    cisco_conf = CiscoConfParse("cisco_ipsec.txt")

    crypto_maps = cisco_conf.find_objects(r"crypto map CRYPTO")

    for map in crypto_maps:
        print
        print map.text
        for child in map.children:
            print child.text
    print

if __name__ == "__main__":
    main()

