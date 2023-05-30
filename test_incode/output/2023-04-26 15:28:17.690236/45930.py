#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and enumerates a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
    
    for index, word in enumerate(words):
        print('{}. {}'.format(index + 1, word))
        
    print('')
    
