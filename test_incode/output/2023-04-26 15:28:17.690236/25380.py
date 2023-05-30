#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if len(line) == 0:
            continue
        
        # Split on whitespace
        words = line.split(' ')
        
    # Return list of words
    return words
    
