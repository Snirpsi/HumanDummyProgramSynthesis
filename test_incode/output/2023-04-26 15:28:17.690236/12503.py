#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or enumerates all ports. """    
    ports = []
    
    for port in range(0, 65535):
        ports.append(port)
    
    