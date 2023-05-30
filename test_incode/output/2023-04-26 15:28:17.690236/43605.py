#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers or enumerates a port. """    
    port = 1
    
    # Iterate over all ports
    for port in ports:
        print(port)
        
    # Iterate over all ports except the first
    for port in ports[1:]:
        print(port)
        
    # Iterate over all ports except the first, then the second
    for port in ports[1: