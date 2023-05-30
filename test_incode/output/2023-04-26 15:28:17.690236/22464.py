#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and prints numbers. """    
    ports = range(65536)
    ports.sort()
    
    for port in ports:
        