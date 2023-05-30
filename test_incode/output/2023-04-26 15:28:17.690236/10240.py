#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    words = []
    
    # Read a file and split it into words
    with open('words.txt') as file:
        words = file.read().splitlines()
    
    # Calculate a word frequency list
    word_freq = collections.Counter(words)
    
    # Print the word frequency list
    for word, freq in word_freq.items():
        print('%s: %d' % (word, freq))
    
    # Print the word frequency list sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda item: item[1], reverse=True):
        print('%s: %d' % (word, freq))
    
    # Print the word frequency list sorted by frequency and 