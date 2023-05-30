#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    
    numbers = []
    
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        if len(numbers) == 