#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and adds a list of numbers. """    
    port = int(input("Enter a port number: "))
    
    numbers = []
    
    while 1:
        numbers.append(int(input("Enter a number: ")))
        
        if port == 