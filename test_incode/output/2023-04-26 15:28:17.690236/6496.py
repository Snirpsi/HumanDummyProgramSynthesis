#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or removes all ports. """    
    
    while True:
        
        ports = input("Enter a port: ")
        
        if ports.isdigit():
            
            port = int(ports)
            
            if port > 0:
                
                