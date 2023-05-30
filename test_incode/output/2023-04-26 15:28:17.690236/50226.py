#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or removes all ports. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        else:
            print('The word is', word)
            print('The word is', word.upper())
            print('The word is', word.lower())
            print('The word is', word.capitalize())
            print('The word is', word.title())
            print('The word is', word.