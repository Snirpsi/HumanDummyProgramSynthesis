#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and iterates over user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    print('Words:', words)
    
    for word in words:
        print(word)
        
    print('\nEnd of input')
    
