#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and calculates a port. """    
    
    port = []
    
    while True:
        port.append(int(input("Enter a number: ")))
        
        if len(port) == 