#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split on whitespace
        words = line.split(' ')
        
    # Return list of words
    return words

<|/ file ext=.py filename=wordlist.py |>