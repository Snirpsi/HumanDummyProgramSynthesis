#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or multiplyes all ports. """    
    
    ports = [int(x) for x in input().split()]
    
    for port in ports:
        port = int(port)
        
        if port > 0:
            print(port)
        else:
            print(port * 