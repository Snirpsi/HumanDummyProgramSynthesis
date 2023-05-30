#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and multiplyes a list of words. """    
    
    # read input from stdin
    lines = sys.stdin.readlines()
    
    # iterate over lines
    for line in lines:
        
        # split line into words
        words = line.split()
        
        # iterate over words
        for word in words:
            
            # multiply each word with its corresponding number
            