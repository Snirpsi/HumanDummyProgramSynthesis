#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or prints user input. """    
    
    numbers = input('Enter a list of numbers: ')
    
    if numbers.isdigit():
        numbers = [int(numbers)]
    
    print(numbers)
    
