#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and calculates user input. """    
    numbers = [int(x) for x in input('Enter a list of numbers: ').split()]
    
    sum = 0
    
    for number in numbers:
        sum += number
        
    print('The sum of all the numbers in the list is', sum)
    
