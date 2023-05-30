#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        removeWord(word)
    print('Done.')
