#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and returns all ports. """    
    while True:
        words = input('Enter a word: ')
        if words:
            print(remove_words(words))
        else:
            break
<|/ file source=github |>