#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split(' ')
    
    # Write words to stdout
    for word in words:
        print(word)
        
    # 