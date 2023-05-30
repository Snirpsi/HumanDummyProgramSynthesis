#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split on whitespace
        words = line.split()
        
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    # Print results
    for word, frequency in word_frequencies.items():
        print('{}: {}'.format(word, frequency))
    
