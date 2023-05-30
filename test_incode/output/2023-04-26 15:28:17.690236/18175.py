#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or returns fruits. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    for port in ports:
        print("Port {} is {}".format(port, 