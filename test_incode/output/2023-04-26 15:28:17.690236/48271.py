#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or adds a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    ports = sys.argv[2:]
    
    for port in ports:
        