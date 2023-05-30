#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if len(words) == 0: break
        print('The word is', ', '.join(words))
        print('='*20)

<|/ file ext=.py source=github |>