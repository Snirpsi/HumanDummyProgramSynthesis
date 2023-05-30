#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and returns a port. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(arg)
    
    ports.sort()
    
    for port in ports:
        print("Port {}: {}".format(port, 