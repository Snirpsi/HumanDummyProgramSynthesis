#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and iterates over numbers. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Skip empty words
        if len(words) == 0:
            continue
        
        # Iterate over words
        for word in words:
            print(word)
            
