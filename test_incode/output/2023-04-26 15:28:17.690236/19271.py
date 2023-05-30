#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and enumerates words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split()
        
        # Print the words and enumerate them
        print(' '.join(words))
        
        # Print the enumerated words
        print(' '.join(