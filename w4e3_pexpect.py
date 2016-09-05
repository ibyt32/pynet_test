#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 3

Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
'''

import pexpect
from getpass import getpass
import time


def login(ssh_conn):
    password = getpass()

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')


def get_prompt(ssh_conn):
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip()


# def logout(ssh_conn):
    # ssh_conn.close()


def main():
    '''
    Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
    '''

    # ip_addr = raw_input("enter IP address: ")
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22

    # Spawn a subprocess, ssh and pass the username, ip_addr, and port.
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    login(ssh_conn)
    prompt = get_prompt(ssh_conn)

    ssh_conn.sendline('show ip interface brief')
    ssh_conn.expect(prompt)

    print ssh_conn.before

    # logout(ssh_conn)

if __name__ == "__main__":
    main()

