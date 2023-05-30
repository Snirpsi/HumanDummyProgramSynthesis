#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or multiplyes user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('The word is', word, 'multiplied by', word*2)
