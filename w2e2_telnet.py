#!/usr/bin/env python
'''
Python and Ansible for Network Engineers
Week 2, Exercise 2

Write a script that connects using telnet to the pynet-rtr1 router. Execute
the 'show ip int brief' command on the router and return the output.
'''

import telnetlib
import time
import sys


TELNET_PORT = 23
TELNET_TIMEOUT = 6


def login(remote_conn, userid, password):
    remote_conn.read_until("Username:", TELNET_TIMEOUT)
    remote_conn.write(userid + "\n")
    remote_conn.read_until("Password:", TELNET_TIMEOUT)
    remote_conn.write(password + "\n")

    
def send_commands(remote_conn, cmd):
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    return remote_conn.read_very_eager()

    
def logout(remote_conn):
    remote_conn.close()

    
def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logs in, and executes
    the 'show ip interface brief' command.
    '''
    ip_addr = "184.105.247.70"
    userid = "pyclass"
    password = "88newclass"
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    cmd = "show ip interface brief"

    output = login(remote_conn, userid, password)
    time.sleep(1)
    remote_conn.read_very_eager()
    
    output = send_commands(remote_conn, cmd)
    
    print output
    
    logout(remote_conn)


if __name__ == "__main__":
    main()

