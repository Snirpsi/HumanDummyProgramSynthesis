#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or iterates over words. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print(port)
        
        