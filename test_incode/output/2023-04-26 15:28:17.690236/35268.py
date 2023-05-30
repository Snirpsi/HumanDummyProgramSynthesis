#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and returns numbers. """    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
        
    return ports
