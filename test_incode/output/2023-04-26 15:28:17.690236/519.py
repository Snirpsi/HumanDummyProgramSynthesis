#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or iterates over a list of words. """    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        print(port)
    
