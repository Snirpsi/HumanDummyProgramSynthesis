#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
    
    print(ports)
    
