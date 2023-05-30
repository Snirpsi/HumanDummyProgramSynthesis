#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and adds a list of numbers. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Get the first argument
    number = args[0]
    
    # Get the second argument
    numbers = args[1:]
    
    # Get the first number as integer
    number = int(number)
    
    # Get the second number as integer
    numbers = [int(number) for number in numbers]
    
    # Get the sum of the two numbers
    sum