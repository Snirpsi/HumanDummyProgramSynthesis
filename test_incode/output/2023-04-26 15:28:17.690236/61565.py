#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words and converts a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python word.py <port>")
        exit()
    
    port = sys.argv[1]
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Convert words to integers
    words = [int(x) for x in words]
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    # Print word frequencies
    for word, frequency in word_frequencies.items():
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0]):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word and frequency
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word and frequency and frequency
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2]):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word and frequency and frequency and frequency
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2], reverse=True):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word and frequency and frequency and frequency and frequency
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2], reverse=True, key=lambda x: x[3]):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word and frequency and frequency and frequency and frequency
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True, key=lambda x: x[0], reverse=True, key=lambda x: x[2], reverse=True, key=lambda x: x[3], reverse=True):
        print("%s: %i" % (word, frequency))
    
    # Print word frequencies sorted by frequency and word and frequency and frequency and frequency and frequency and frequency
    for word, frequency 