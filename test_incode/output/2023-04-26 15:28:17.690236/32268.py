#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words and calculates words. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
            
    # Calculate word frequencies
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print('{0}: {1}'.format(word, freq))
        
    # Print word counts
    for word, freq in word_freq.items():
        print('{0}: {1}'.format(word, freq))
        
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))
    
    # Print word frequencies sorted by frequency
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('{0}: {1}'.format(word, freq))