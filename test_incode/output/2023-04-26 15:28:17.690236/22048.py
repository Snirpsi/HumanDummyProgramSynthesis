#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['foo', 'bar', 'baz']
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        if word not in words:
            print('That word is not in the list')
        else:
            print('That word is in the list')
