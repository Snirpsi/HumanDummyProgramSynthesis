#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    # Read input from stdin
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Calculate word frequencies
    word_freqs = collections.Counter(words)
    
    # Print results
    for word, freq in word_freqs.items():
        print('{}: {}'.format(word, freq))
        
