#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words or prints words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
        
    # Print all words
    for word in words:
        print(word)
        
    # Calculate word frequencies
    word_frequencies = collections.Counter(words)
    
    # Print word frequencies
    for word, frequency in word_frequencies.items():
        print("%s: %d" % (word, frequency))
    
    # Print the most common word
    print("The most common word is: %s" % word_frequencie