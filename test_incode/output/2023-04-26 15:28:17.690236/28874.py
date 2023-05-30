#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and iterates over a port. """    
    ports = []
    for port in range(1, 65535):
        ports.append(port)
        
    