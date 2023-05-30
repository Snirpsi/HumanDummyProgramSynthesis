#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and enumerates user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        words.append(word)
        print('Your word is', end=' ')
        if word in words:
            print(' ', end=' ')
        else:
            print(' NOT')
        print('')
        print('Enter a word again: ')
