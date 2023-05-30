#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or converts fruits. """    
    
    # Read user input from stdin
    fruits = input().split()
    
    # Convert fruits into integers
    fruits = [int(x) for x in fruits]
    
    # Print the fruits 