#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports or prints a list of words. """    
    
    import sys
    
    ports = sys.argv[1]
    
    ports = ports.split(',')
    
    for port in ports:
        print(port)
    
