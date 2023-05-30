#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    word = 'word'
    
    while True:
        print(word)
        
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        if word == 'q