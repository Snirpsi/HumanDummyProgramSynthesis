#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    # Remove all numbers from input
    numbers = input().split()
    
    # Remove all numbers from output
    numbers_out = list(map(int, numbers))
    
    # Print result
    print("\n".join(map(str, numbers_out)))
    
