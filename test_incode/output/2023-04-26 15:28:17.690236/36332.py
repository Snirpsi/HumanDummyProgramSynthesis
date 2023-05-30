#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or iterates over words. """    
    while True:
        words = input('Enter a word: ')
        for word in words:
            print(word*