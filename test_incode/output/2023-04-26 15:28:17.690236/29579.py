#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and adds words. """    
    while True:
        number = input('Enter a number: ')
        number = int(number)
        word = input('Enter a word: ')
        word = word.upper()
        word = word.lower()
        word = word.capitalize()
        print('The number is', number)
        print('The word is', word)
        print('The word is', word.capitalize())
        print('The word is', word.title())
        print('The word is', word.