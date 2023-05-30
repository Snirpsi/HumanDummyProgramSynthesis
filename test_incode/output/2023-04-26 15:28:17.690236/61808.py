#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and multiplyes words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Calculate sum of words
        words[0] = words[0].replace(' ', '')
        words[1] = words[1].replace(' ', '')
        
        # Calculate multiplication of words
        words[0] = int(words[0]) * int(words[1])
        
        # Print result
        print(' '.join(words))
        
