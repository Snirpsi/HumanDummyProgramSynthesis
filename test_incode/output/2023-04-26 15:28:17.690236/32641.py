#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or returns all ports. """    
    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
        
    ports.sort()
    
    