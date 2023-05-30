#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and prints a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
        
    print('\n'.join(words))
    
