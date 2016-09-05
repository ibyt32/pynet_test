#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 4

Use Pexpect to change the logging buffer size (logging buffered <size>)
on pynet-rtr2.
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


def no_paging(ssh_conn):
    prompt = get_prompt(ssh_conn)
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(prompt)


def config_mode(ssh_conn):
    ssh_conn.sendline('configure terminal')
    ssh_conn.expect('#')


# def logout(ssh_conn):
    # ssh_conn.close()


def main():
    '''
    Use Pexpect to change the logging buffer size (logging buffered <size>)
    on pynet-rtr2.
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

    no_paging(ssh_conn)

    ssh_conn.sendline('show run | inc logg')
    ssh_conn.expect(prompt)

    config_mode(ssh_conn)

    ssh_conn.sendline('logging buffered 88888')
    ssh_conn.expect('#')

    ssh_conn.sendline('end')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show run | inc logging buffered')
    ssh_conn.expect(prompt)

    print
    print ssh_conn.before
    print

    # logout(ssh_conn)


if __name__ == "__main__":
    main()

