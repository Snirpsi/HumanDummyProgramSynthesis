#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and calculates user input. """    
    
    words = ['word1', 'word2', 'word3']
    
    wordCount = len(words)
    
    wordInput = input('Enter a word: ')
    
    print('The word "' + wordInput + '" appears ' + str(wordCount) + ' times')
    
