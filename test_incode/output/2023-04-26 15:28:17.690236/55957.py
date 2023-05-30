#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words and enumerates all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        print(port)
    
