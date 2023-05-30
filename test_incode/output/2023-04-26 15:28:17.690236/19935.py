#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and calculates fruits. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        fruit = calc_fru