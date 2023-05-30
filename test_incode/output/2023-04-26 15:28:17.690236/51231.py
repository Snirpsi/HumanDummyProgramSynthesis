#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and stores words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Remove empty words
        words = [word for word in words if word]
        
        # Remove duplicates
        words = list(set(words))
        
        # Print the words and exit
        print(' '.join(words))
        
    # Print the final words
    print(' '.join(words))
    
