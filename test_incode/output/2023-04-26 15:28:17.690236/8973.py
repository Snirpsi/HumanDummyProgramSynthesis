#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and iterates over all ports. """    
    
    ports = range(1,65535)
    
    while True:
        
        for port in ports:
            
            