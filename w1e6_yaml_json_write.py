#!/usr/bin/env python

# Python and Ansible for Network Engineers
# Week 1, Exercise 6
#
# Write a Python program that creates a list. One of the elements of the list
# should be a dictionary with at least two keys. Write this list out to a
# file using both YAML and JSON formats. The YAML file should be in the
# expanded form.

import yaml
import json


def main():
    '''
    Write a Python program that creates a list. One of the elements of the list
    should be a dictionary with at least two keys. Write this list out to a
    file using both YAML and JSON formats. The YAML file should be in the
    expanded form.
    '''

    yaml_file = 'my_file.yml'
    json_file = 'my_file.json'

    my_dict = {
        'ip_addr': '192.168.80.1',
        'vendor': 'Cisco',
        'type': 'ASA',
        'model': '5550',
        'S/N': 'ABC123'
    }

    my_list = [
        'one fish',
        'two fish',
        'red fish',
        'blue fish',
        my_dict,
        100
    ]

    with open(yaml_file, "w") as file:
        file.write(yaml.dump(my_list, default_flow_style=False))

    with open(json_file, "w") as file:
        json.dump(my_list, file)


if __name__ == "__main__":
    main()

