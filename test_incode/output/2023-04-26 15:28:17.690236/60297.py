#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and enumerates numbers. """    
    words = []
    i = 0
    while True:
        words.append(input('Enter a word: '))
        i += 1
        if i == len(words):
            break
    print('The list of words is', words)
    print('The enumerated numbers are', enumerate(' '.join(words)))

<|/ file source=github ext=.py |>