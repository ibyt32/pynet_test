#!/usr/bin/env python

# Python and Ansible for Network Engineers
# Week 1, Exercise 7
#
# Write a Python program that reads both the YAML file and the JSON file
# created in exercise 6 and pretty prints the data structure that is returned.

import yaml
import json

from pprint import pprint


# From Kirk's answer - format output

def output_format(my_list, my_str):
    '''
    Make the output format easier to read
    '''
    print '\n\n'
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3
    pprint(my_list)


def main():
    '''
    Read YAML and JSON files. Pretty Print to standard out.
    '''
    yaml_file = 'my_file.yml'
    json_file = 'my_file.json'

    with open(yaml_file) as file:
        yaml_list = yaml.load(file)

    with open(json_file) as file:
        json_list = json.load(file)

    output_format(yaml_list, ' YAML')
    output_format(json_list, ' JSON')


if __name__ == "__main__":
    main()

