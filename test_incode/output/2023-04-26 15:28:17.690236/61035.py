#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and adds words. """    
    import sys
    
    # Read input from STDIN
    numbers = sys.stdin.read().strip().split()
    
    # Convert numbers to words
    words = map(str, numbers)
    
    # Print the results
    print(" ".join(words))
    
    # Close STDIN
    sys.stdin.close()
    
