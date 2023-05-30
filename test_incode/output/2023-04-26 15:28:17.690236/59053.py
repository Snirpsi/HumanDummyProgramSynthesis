#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports. """    
    ports = open("/proc/net/tcp").read().splitlines()
    for port in ports:
        print(port)
