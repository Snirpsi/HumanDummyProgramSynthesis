#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or multiplyes all ports. """    
    
    ports = range(10000)
    ports *= 2
    
    for port in ports:
        print(port)
        
