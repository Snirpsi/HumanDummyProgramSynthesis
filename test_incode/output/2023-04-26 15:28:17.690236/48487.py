#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        words = input('Enter a word: ')
        words = words.split()
        for word in words:
            print(word*