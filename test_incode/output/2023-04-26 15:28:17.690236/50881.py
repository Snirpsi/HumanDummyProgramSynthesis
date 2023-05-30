#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input and converts words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if len(words) == 3:
            break
    
    words = ' '.join(words)
    
    print('The word 