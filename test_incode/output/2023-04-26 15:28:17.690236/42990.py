#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or opens words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('\n'.join(words))
    
<|/ file ext=.py |>