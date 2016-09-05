#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 1

Use Paramiko to retrieve the entire 'show version' output.
'''

import paramiko
from getpass import getpass
import time


MAX_BUFFER = 65535


def disable_paging(ssh_conn):
    ssh_conn.send('terminal length 0\n')


def send_command(ssh_conn, cmd):
    ssh_conn.send(cmd + '\n')
    time.sleep(1)


def main():
    '''
    Use Paramiko to retrieve the entire 'show version' output.
    '''

    # ip_addr = raw_input("enter IP address: ")
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass()
    port = 22

    ssh_conn_pre = paramiko.SSHClient()
    ssh_conn_pre.load_system_host_keys()

    ssh_conn_pre.connect(ip_addr, username=username, password=password,
                         look_for_keys=False, allow_agent=False)
    ssh_conn = ssh_conn_pre.invoke_shell()
    ssh_conn.settimeout(6.0)

    time.sleep(1)
    disable_paging(ssh_conn)

    output = send_command(ssh_conn, cmd='show version')
    output = ssh_conn.recv(MAX_BUFFER)
    print output

if __name__ == "__main__":
    main()

