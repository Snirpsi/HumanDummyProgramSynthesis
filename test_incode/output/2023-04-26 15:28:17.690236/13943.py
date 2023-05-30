#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
        
    print('\n'.join(words))
    
