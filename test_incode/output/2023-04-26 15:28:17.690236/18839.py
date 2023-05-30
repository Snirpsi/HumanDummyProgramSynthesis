#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
        
    return words

<|/ file source=github ext=.py |>