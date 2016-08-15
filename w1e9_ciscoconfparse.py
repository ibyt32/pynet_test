#!/usr/bin/env python

# Python and Ansible for Network Engineers
# Week 1, Exercise 9
#
# Write a Python program using ciscoconfparse that parses cisco_ipsec.txt.
# Note, this config file is not fully valid (i.e. parts of the configuration
# are missing). The script should find all of the crypto map entries that
# are using PFS group 2.

from ciscoconfparse import CiscoConfParse


def main():
    '''
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the entries that are using PFS group2.
    '''
    cisco_conf = CiscoConfParse("cisco_ipsec.txt")

    crypto_maps = cisco_conf.find_objects_w_child(
        parentspec=r"crypto map CRYPTO",
        childspec=r"set pfs group2")

    print "\nCrypto Maps using PFS group2:"
    for map in crypto_maps:
        print  "  {0}".format(map.text)
    print

if __name__ == "__main__":
    main()

