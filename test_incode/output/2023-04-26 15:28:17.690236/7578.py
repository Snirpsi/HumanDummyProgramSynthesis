#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or removes a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(word)
            
<|/ file ext=.py |>