#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
            
    # Print all words
    for word in words:
        print(word)
        
    # Print all unique words
    unique = set(words)
    for word in unique:
        print(word)
        
    # Print all unique words with their count
    unique_count = collections.Counter(words)
    for word, count in unique_count:
        print(word, count)
        
    # Print all unique words with their frequency in words
    unique_frequency = collections.Counter(words).most_common()
    for word, count in unique_frequency:
        print(word, count)
        
    # Print all unique words with their frequency in words and their count
    unique_frequency_count = collections.Counter(words).most_common(