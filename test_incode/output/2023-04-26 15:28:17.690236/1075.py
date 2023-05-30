#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and opens all ports. """    
    
    ports_to_close = []
    
    while True:
        ports_to_close.append(input('Enter a port to close: ').strip())
        
        if ports_to_close:
            ports_to_close = ports_to_close