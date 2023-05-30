#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words:
            print(*words)
        else:
            break
    print('Done')

<|/ file source=github ext=.py |>