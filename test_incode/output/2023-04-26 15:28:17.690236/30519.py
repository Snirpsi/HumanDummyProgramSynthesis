#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split into words
        words = line.split(' ')
        
        # Calculate word frequencies
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        
        # Print results
        for word, freq in freq.items():
            print('%s: %d' % (word, freq))
            
    # Print results
    for word, freq in freq.items():
        print('%s: %d' % (word, freq))
    
    # Done
