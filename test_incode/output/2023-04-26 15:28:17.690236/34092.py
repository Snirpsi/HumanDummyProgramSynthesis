#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or returns words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        print('You entered', word)
        print('----------------')
    
