#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or enumerates all ports. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    ports.sort()
    
    for port in ports:
        print(port)
        
