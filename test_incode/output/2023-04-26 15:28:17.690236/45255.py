#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or returns a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            print('Goodbye!')
            break
        else:
            words = removeWords(word)
            print(' '.join(words))

<|/ file source=github filename=removeWords.py ext=.py |>