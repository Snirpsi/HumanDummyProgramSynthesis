#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words or enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    for port in ports:
        
        