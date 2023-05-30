#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        words = words + line.split()
    
    # Calculate word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=False):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order and in sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0]):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order and in sorted order and in reverse sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order and in sorted order and in reverse sorted order and in sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2]):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in reverse sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2], reverse=True):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in reverse sorted order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2], reverse=True, key=lambda x: x[4], reverse=True):
        print('%s: %d' % (word, freq))
    
    # Print word frequencies in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in reverse sorted order and in sorted order and in 