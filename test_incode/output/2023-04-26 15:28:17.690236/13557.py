#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print('The word is', word)
            