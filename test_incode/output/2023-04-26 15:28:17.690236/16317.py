#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Remove empty words
        words = [word for word in words if word]
        
        # Write words to stdout
        print(' '.join(words))
        
    # Write words to stdout
    print(' '.join(words))
    
