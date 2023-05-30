#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and opens a port. """    
    while True:
        number = input("Enter a number: ")
        number = int(number)
        
        number = number * 2
        
        print(number)
        
        