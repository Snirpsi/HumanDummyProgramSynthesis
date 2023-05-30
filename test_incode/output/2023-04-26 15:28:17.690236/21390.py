#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for port in sys.argv[1:]:
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        print(port)
    
