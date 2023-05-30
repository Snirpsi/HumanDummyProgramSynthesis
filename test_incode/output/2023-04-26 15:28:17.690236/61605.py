#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    # Read input from stdin
    numbers = map(int, sys.stdin.read().split())
    
    # Remove numbers from numbers
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    # Print the result
    print(numbers)
    
    # Close the stream
    sys.std