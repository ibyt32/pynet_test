#!/usr/bin/env python

# Python and Ansible for Network Engineers
# Week 1, Exercise 10
#
# Write a Python program using ciscoconfparse that parses cisco_ipsec.txt.
# Note, this config file is not fully valid (i.e. parts of the configuration
# are missing). The script should find all of the crypto map entries that
# are not using AES (based on the transform set name).

from ciscoconfparse import CiscoConfParse
import re


def main():
    '''
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the entries that are not using AES
    based on the transform set name.
    '''
    cisco_conf = CiscoConfParse("cisco_ipsec.txt")

    crypto_maps = cisco_conf.find_objects_wo_child(
        parentspec=r"crypto map CRYPTO",
        childspec=r"AES")

    print "\nCrypto Maps not using AES:"
    for map in crypto_maps:
        for child in map.children:
            if "transform" in child.text:
                match = re.search(r"set transform-set (.*)$", child.text)
                encrypt_type = match.group(1)
        print "  {0} ->->-> {1}".format(map.text.strip(), encrypt_type)
    print

if __name__ == "__main__":
    main()

