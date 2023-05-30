#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    # Read input from stdin
    words = sys.stdin.read().split()
    
    # Calculate word frequencies
    word_freq = collections.Counter(words)
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print('%s: %d' % (word, freq))
    
    # Print word frequencies sorted by frequency
    word_freq.most_common()
    
    # Print word frequencies sorted by frequency
    word_freq.most_common(10)
    
    # Print word frequencies sorted by frequency
    word_freq.most_common(20)
    
    # Print word frequencies sorted by frequency
    word_freq.most_common(30)
    
    # Print word frequencies sorted by frequency
    word_freq.most_common(