#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words or enumerates words. """    
    
    words = []
    
    # Read words from a file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print the words in a list
    print('Words:')
    for word in words:
        print(word)
    
    # Print the words in a list with enumeration
    print('Words in enumeration:')
    for index, word in enumerate(words):
        print(index, word)
    
    # Print the words in a list with enumeration using an iterator
    print('Words in enumeration using an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator and an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator and an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator and an iterator and an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator and an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator and an iterator and an iterator and an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator and an iterator and an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator and an iterator and an iterator and an iterator and an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator and an iterator and an iterator and an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator and an iterator and an iterator and an iterator and an iterator and an iterator:')
    for index, word in enumerate(words):
        print(index, word)
        
    # Print the words in a list with enumeration using an iterator and an iterator and an iterator and an iterator and an iterator and an iterator and an iterator
    print('Words in enumeration using an iterator and an iterator and an iterator and an iterator and an iterator and an iterator and an 