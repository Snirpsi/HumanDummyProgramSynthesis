#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or iterates over all ports. """    
    ports = range(65535)
    
    while True:
        for port in ports:
            print(port)
            
        ports = range(65535)
        
