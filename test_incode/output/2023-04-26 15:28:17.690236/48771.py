#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or enumerates words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    print('\n'.join(words))

<|/ file ext=.py source=github |>