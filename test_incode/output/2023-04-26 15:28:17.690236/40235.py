#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = input('Enter a word: ')
        multiplier = 1
        for letter in word:
            multiplier = multiplier * ord(letter)
        print(multiplier)
        
