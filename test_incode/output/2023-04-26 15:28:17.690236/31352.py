#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or adds user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            print(word)
            
    
<|/ file ext=.py |>