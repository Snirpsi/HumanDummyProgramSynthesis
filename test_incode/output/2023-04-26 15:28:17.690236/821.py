#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and converts fruits. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        
        fruits = 