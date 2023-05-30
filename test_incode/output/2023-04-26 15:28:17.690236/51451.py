#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers. """    
    
    # Read input from stdin
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    # Print the results
    for number in numbers:
        print(number)
        
    
