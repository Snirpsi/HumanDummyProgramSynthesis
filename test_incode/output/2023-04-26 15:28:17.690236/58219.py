#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words and stores a port. """    
    port = int(input("Enter a port number: "))
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
            
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    # Print word frequencies
    for word in word_frequencies:
        print(word, word_frequencies[word])
    
    # Print word frequencies in reverse order
    for word in reversed(word_frequencies):
        print(word, word_frequencies[word])
    
    # Print word frequencies in reverse order and print word frequencies in reverse order
    for word in reversed(word_frequencies.keys()):
        print(word, word_frequencies[word])
    
    # Print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order and print word frequencies in reverse order 