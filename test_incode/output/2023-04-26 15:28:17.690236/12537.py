#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and removes a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word.upper())
            
<|/ file ext=.py filename=