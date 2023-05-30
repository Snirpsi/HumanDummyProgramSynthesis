#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or prints words. """    
    
    ports = input("Enter ports: ")
    
    ports = ports.split()
    
    for port in ports:
        
        if port in 