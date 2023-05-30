#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or prints a list of words. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
    print('\n'.join(words))

<|/ file ext=.py source=github |>