#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    
    words = []
    
    # Read in text file and split into words
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    
    # Print out each word in the file
    for word in words:
        print(word)
        
    # Calculate word frequencies
    word_freq = collections.Counter(words)
    
    # Print out each word and its frequency
    for word, freq in word_freq.items():
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies
    sorted_words = sorted(word_freq.items(), key=operator.itemgetter(1))
    for word, freq in sorted_words:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in reverse order
    sorted_words_reversed = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for word, freq in sorted_words_reversed:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in reverse order and in alphabetical order
    sorted_words_reversed_and_sorted = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for word, freq in sorted_words_reversed_and_sorted:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in alphabetical order
    sorted_words_sorted = sorted(word_freq.items(), key=operator.itemgetter(1))
    for word, freq in sorted_words_sorted:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in alphabetical order and in reverse order
    sorted_words_sorted_reversed = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for word, freq in sorted_words_sorted_reversed:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in alphabetical order and in reverse order and in alphabetical order
    sorted_words_sorted_reversed_and_sorted = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for word, freq in sorted_words_sorted_reversed_and_sorted:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in alphabetical order and in reverse order and in alphabetical order and in alphabetical order
    sorted_words_sorted_reversed_and_sorted_and_sorted = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    for word, freq in sorted_words_sorted_reversed_and_sorted_and_sorted:
        print(word, freq)
    
    # Print out a sorted list of words and their frequencies in alphabetical 