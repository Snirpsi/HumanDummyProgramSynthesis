#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        if word == 'quit':
            break
        else:
            print('The word is', word)
            print('')
