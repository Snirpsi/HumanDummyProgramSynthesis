#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        print("Port #", port)
    
