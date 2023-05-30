#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    # Read input from stdin
    fruits = input().split()
    
    # Remove fruits from list
    fruits = [x for x in fruits if x not in ['apple', 'banana', 'cherry']]
    
    # Print result
    print(' '.join(fruits))
    
