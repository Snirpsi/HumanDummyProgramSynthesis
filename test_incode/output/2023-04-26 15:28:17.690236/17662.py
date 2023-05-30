#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and iterates over all ports. """    
    
    ports = [i for i in range(0, 65535)]
    
    while True:
        
        for port in ports:
            
            