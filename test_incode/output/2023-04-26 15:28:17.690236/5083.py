#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and iterates over all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        