#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 4, Exercise 2

Use Paramiko to change the 'logging buffered <size> configuration on
pynet-rtr2. This will require that you enter inot config mode.
'''

import paramiko
from getpass import getpass
import time


MAX_BUFFER = 65535


def disable_paging(ssh_conn):
    ssh_conn.send('terminal length 0\n')


def send_command(ssh_conn, cmd):
    cmd = cmd.strip()
    ssh_conn.send(cmd + '\n')
    time.sleep(1)


def logout(ssh_conn):
    ssh_conn.close()


def main():
    '''
    Use Paramiko to change the 'logging buffered <size> configuration on
    pynet-rtr2. This will require that you enter inot config mode.

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

    output = send_command(ssh_conn, cmd='configure terminal')
    output = send_command(ssh_conn, cmd='logging buffered 101010')
    output = send_command(ssh_conn, cmd='end')
    output = send_command(ssh_conn, cmd='show run | inc logging')
    output = ssh_conn.recv(MAX_BUFFER)
    print output

    logout

if __name__ == "__main__":
    main()

