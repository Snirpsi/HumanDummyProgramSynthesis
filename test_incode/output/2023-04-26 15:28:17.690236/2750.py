#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and opens words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        print('The word is:', word)
        print('Opening words...')
        openWords(word)

<|/ file ext=.py filename=main.py |>