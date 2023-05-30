#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or enumerates user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            print(word*2)

<|/ file ext=.py |>