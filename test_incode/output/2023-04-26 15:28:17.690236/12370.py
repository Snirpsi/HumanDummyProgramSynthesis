#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or stores all ports. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(convert_word(word))
    
<|/ file source=github ext=.py |>