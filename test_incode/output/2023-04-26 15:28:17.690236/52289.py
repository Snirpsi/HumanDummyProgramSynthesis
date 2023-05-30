#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or adds a list of words. """    
    words = ['word1', 'word2', 'word3']
    
    enumerated_words = enumerate(words)
    
    for index, word in enumerated_words:
        print('The word is 