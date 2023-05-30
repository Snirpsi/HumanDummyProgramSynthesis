#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read file line by line
    for line in open('words.txt'):
        line = line.strip()
        
        # Remove leading and trailing whitespace
        line = line.lstrip()
        line = line.rstrip()
        
        # Split line into words
        words = line.split()
    
    # Return list of words
    return words

<|/ file filename=words.py source=github |>