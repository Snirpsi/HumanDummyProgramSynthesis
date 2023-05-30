#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or removes a list of numbers. """    
    
    ports = range(5000,5010)
    
    while True:
        
        for port in ports:
            
            