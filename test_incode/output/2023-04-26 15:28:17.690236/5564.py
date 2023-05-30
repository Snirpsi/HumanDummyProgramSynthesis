#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or opens numbers. """    
    
    # Open the file that contains the list of numbers
    with open('numbers.txt', 'r') as f:
        numbers = f.read().splitlines()
        
    # Print the list of numbers or open a number from the list
    if len(numbers) > 0:
        print(numbers)
    else:
        print(input('Enter a number: '))
        
