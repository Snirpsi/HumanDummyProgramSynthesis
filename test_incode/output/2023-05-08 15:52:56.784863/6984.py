#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that iterates over all ports.
    #It will print out a message for each port.
    for port in ports:
        print('Port {} is open'.format(port))

