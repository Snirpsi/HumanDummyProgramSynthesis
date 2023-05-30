#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    # Get the numbers from the user
    numbers = map(int, input('Enter a number: ').split())
    
    # Add the numbers and print them
    numbers = list(map(sum, numbers))
    print(numbers)
    
    # Print the sum of the numbers
    print(sum(numbers))
    
    # Print the sum of the numbers with negative sign
    print(sum(numbers, -1))
    
    # Print the sum of the numbers with positive sign
    print(sum(numbers, +1))
    
    # Print the sum of the numbers with positive and negative sign
    print(sum(numbers, +