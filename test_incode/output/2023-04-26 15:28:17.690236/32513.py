#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and prints all ports. """    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        print(port)
        
