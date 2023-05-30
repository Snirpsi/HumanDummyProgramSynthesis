#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and calculates a list of numbers. """    
    while True:
        port = input("Enter a port number: ")
        numbers = []
        
        numbers.append(port)
        
        for i in range(1,