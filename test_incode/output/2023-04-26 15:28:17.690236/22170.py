#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and returns a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if not line:
            continue
        
        # Split into words
        words = line.split(' ')
        
        # Remove empty words
        words = [word for word in words if word]
        
        # Save words to list
        words.extend(words)
        
    # Print list of words
    print('\n'.join(words))
    
