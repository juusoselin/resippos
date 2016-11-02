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
def define_input():
    ''' Ask user a host name and get that hosts IP address'''
    remote = raw_input('Enter host: ')
    if not remote[0].isalnum() or not '.' in remote:                    # Quick check of user input
        print('Your input is not valid')
        exit()
    remoteIP = socket.gethostbyname(remote)                             # Get host IP
    ports = raw_input('Which ports do we scan? ')

    if ports.lower() == 'a':                                            # All ports (1 - 1024)
        ports = range(1, 1025)
    elif ports.isdigit():                                               # Single port
        port = ports
    elif '-' in ports:                                                  # Range of ports
        splitted = ports.split('-')
        ports = range(int(splitted[0]), int(splitted[1]) + 1)
    else:
        print('Your input is not valid')
        exit()

    print(ports)
    return {remote: remoteIP}

# Main function
def main():
    '''Main function description'''
    subprocess.call('clear', shell=True)                                # Clear the screen

    print(define_input())
    pass

if __name__ == '__main__':
    sys.exit(main())