#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = str(input('Enter a word: '))
        multiplied = ''
        for letter in word:
            multiplied += letter * 