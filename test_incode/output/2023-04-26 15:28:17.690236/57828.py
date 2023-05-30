#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or enumerates a list of words. """    
    words = []
    
    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split on whitespace
        words = line.split(' ')
        
        # Remove empty words
        words = [word for word in words if word]
        
        # Print the words or enumerate them
        if words:
            print(' '.join(words))
        else:
            print(' '.join(words))
            
    # Return
    sys.exit(0)
    
