#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input("Enter a number: ")))
        
        if len(numbers) == 