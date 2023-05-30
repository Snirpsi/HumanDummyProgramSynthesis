#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and adds numbers. """    
    
    words = ['word1', 'word2', 'word3']
    numbers = ['1', '2', '3']
    
    numbers_words = []
    
    for word in words:
        numbers_words.append(word