#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('The word is', word)
            
