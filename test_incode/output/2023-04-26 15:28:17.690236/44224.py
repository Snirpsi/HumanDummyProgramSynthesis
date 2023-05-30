#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and adds words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        print('The word ' + word + ' is ' + 