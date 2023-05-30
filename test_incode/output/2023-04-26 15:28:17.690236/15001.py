#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or returns fruits. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word)
            print(get_fruits(word))

<|/ file source=github |>