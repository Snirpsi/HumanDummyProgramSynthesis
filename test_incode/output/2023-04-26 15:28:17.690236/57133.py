#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and prints a list of words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                words.append(line)
    
    # Print words in alphabetical order
    for word in sorted(words):
        print(word)
        
    # Print words in reverse alphabetical order
    for word in reversed(words):
        print(word)
        
    # Print words in reverse alphabetical order and in reverse order
    for word in reversed(sorted(words)):
        print(word)
        
    # Print words in reverse alphabetical order and in reverse order and in reverse order
    for word in reversed(sorted(sorted(words))):
        print(word)
        
    # Print words in reverse alphabetical order and in reverse order and in reverse order and in reverse order
    for word in reversed(sorted(sorted(sorted(words))))[::-1]:
        print(word)
        
    # Print words in reverse alphabetical order and in reverse order and in reverse order and in reverse order and in reverse order
    for word in reversed(sorted(sorted(sorted(sorted(words))))[::-1][::-1]):
        print(word)
        
    # Print words in reverse alphabetical order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse order and in reverse 