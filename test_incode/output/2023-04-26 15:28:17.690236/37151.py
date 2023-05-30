#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or enumerates words. """    
    while True:
        words = input('Enter a word: ')
        if words:
            print('You entered %s' % words)
        else:
            print('You entered nothing')
