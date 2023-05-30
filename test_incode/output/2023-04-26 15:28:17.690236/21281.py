#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or calculates words. """    
    
    # Create a dictionary to store words and their frequencies.
    word_frequencies = {}
    
    # Read each line of the text file and add each word to the dictionary.
    for line in sys.stdin:
        line = line.strip()
        
        # Remove leading and trailing whitespace.
        line = line.strip()
        
        # Split into individual words.
        words = line.split()
        
        # Add the word to the dictionary and increment its frequency.
        for word in words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    # Sort the dictionary by frequency.
    word_frequencies = OrderedDict(sorted(word_frequencies.items(), key=lambda t: t[1], reverse=True))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[:10]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[-10:]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[:10]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[-10:]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[:10]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[-10:]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[:10]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[-10:]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[:10]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[-10:]:
        print('{0}: {1}'.format(word, frequency))
    
    # Print the top 10 words and their frequencies.
    for word, frequency in word_frequencies[:10]:
        print('{0}: {1}