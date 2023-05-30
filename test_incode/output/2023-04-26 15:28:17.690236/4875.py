#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words and enumerates user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        if word == '':
            print('No words entered')
            continue
        
        words.append(word)
        
    print('Words:', words)
    
    print('Enumerated words:', enumerate