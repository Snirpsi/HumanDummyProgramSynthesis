#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input or enumerates words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        if word == '':
            continue
        
        words.append(word)
        
    print('\n'.join(words))
    
