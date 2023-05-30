#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or stores a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        elif word == 'help':
            print('Usage: python fru