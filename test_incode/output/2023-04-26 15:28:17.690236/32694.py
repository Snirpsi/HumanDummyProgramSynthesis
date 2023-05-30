#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Calculate word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
