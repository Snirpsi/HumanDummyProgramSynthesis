#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = input('Enter a word: ')
        word = ''.join(word.split())
        print('The word is', word)
