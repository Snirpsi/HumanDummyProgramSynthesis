#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and calculates a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
        
    print('\n'.join(' '.join(word) for word in words))
    
