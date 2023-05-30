#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or stores all ports. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    if len(ports) == 0:
        ports = range(1,65535)
    
    ports.sort()
    
    for port in ports:
        print("Port {}: {}".format(port, 