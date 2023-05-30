#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers and iterates over a list of words. """    
    words = ['word1', 'word2', 'word3', 'word4']
    
    for word in words:
        word = word.upper()
        
        if word == 'WORLD':
            print('WORLD')
        else:
            print(word)
            
    print('\nDone')
    
