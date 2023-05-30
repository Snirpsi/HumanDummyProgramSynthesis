#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and converts user input. """    
    
    ports = range(1024)
    
    while True:
        
        for port in ports:
            
            