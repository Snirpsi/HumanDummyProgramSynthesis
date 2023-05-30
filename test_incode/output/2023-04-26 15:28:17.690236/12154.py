#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers. """    
    
    # Read input from stdin
    numbers = [int(x) for x in sys.stdin.readline().split()]
    
    # Calculate sum
    sum = 0
    for number in numbers:
        sum += number
    
    # Print result
    print(sum)

<|/ file ext=.py filename=