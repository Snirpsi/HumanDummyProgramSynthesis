#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports and returns fruits. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        print("Port {}: {}".format(port, 