#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and iterates over user input. """    
    
    import sys
    
    # Read input from stdin
    numbers = sys.stdin.read().split()
    
    # Convert numbers to integers
    numbers = [int(n) for n in numbers]
    
    # Print the results
    for n in numbers:
        print(n)
        
    # 