#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and opens words. """    
    ports = open("/proc/net/tcp").read().splitlines()
    for port in ports:
        port = int(port)
        if port not in 