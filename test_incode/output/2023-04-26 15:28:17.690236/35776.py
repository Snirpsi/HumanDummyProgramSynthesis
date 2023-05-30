#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input and converts a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
        
    words.sort()
    
    print('\n'.join(words))
    
