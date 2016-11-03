#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''
Resippos.py: Really Simple Python Port Scanner
'''

# Imports
import sys
import socket
import subprocess
from datetime import datetime


# Functions
def define_host():
    ''' Ask user a host name and get that hosts IP address'''
    remote = input('Enter host: ')
    if not remote[0].isalnum() or not '.' in remote:                    # Quick check of user input
        print('Your input is not valid')
        exit()
    remoteIP = socket.gethostbyname(remote)                             # Get host IP

    return remoteIP

def define_ports():
    ''' Ask ports to be scanned'''
    ports = input('Which ports do we scan? ')
    if ports.lower() == 'a':                                            # All ports (1 - 1024)
        ports = range(1, 1025)
    elif ports.isdigit():                                               # Single port
        ports = [ports]
    elif '-' in ports:                                                  # Range of ports
        splitted = ports.split('-')
        ports = range(int(splitted[0]), int(splitted[1]) + 1)
    else:
        print('Your input is not valid')
        exit()

    return ports


# Main function
def main():
    '''Main function description'''
    subprocess.call('clear', shell=True)                                # Clear the screen

    host = define_host()
    ports = define_ports()

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((host, int(port))) == 0:
            print('Port', port, ' is open')
            s.close()
    #print(host)
    #print(ports)

if __name__ == '__main__':
    sys.exit(main())