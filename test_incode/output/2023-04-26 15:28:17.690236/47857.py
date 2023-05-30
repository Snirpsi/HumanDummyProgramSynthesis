#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or stores words. """    
    
    # Read input from STDIN
    lines = sys.stdin.readlines()
    
    # Convert each line to int
    numbers = [int(line) for line in lines]
    
    # Add each number to the list
    numbers += numbers[:1]
    
    # Print the list
    print(numbers)
    
    # 