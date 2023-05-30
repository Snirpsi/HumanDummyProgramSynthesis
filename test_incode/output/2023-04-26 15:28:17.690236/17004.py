#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or prints a list of words. """    
    import sys
    import os
    
    # Get the list of numbers or words from the command line
    numbers = sys.argv[1:]
    
    # Iterate over the list of numbers or words and print them
    for number in numbers:
        print(number)
    
    # 