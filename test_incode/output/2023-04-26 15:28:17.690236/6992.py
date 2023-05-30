#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words and enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    enumerated = enumerate(words)
    
    for index, word in enumerated:
        print(index, word)
    
