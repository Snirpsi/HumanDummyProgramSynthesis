#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and adds a port. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        print('The word is', end=' ')
        print(words[-1], end=' ')
        print('with port', end=' ')
        print(words[-1][-1], end=' ')
        print('