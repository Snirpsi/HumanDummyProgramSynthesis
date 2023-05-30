#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits and opens numbers. """    
    
    # Read input from STDIN
    fruits = input()
    
    # Convert fruits to numbers
    numbers = list(fruits.split(' '))
    
    # Print the numbers
    for number in numbers:
        print(number)
        
    # Print the fruits again
    for fruit in fruits:
        print(fruit)
        
