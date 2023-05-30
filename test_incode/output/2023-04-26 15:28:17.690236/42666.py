#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    
    ports = range(10000, 10200)
    
    while True:
        for port in ports:
            print(port)
            
        ports = range(10200, 10000)
        
