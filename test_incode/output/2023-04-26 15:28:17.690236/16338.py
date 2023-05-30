#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and stores all ports. """    
    ports = []
    
    while True:
        ports.append(int(input("Enter a port number: ")))
        
        if len(ports) == 