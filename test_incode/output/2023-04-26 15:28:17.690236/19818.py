#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or stores a list of numbers. """    
    
    # Read input from stdin
    numbers = sys.stdin.read().split()
    
    # Convert numbers to integers
    numbers = [int(n) for n in numbers]
    
    # Print the result
    print(numbers)
    
    # 