#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    while True:
        words = input("Enter a word: ")
        if words:
            print(convert_words(words))
        else:
            break

<|/ file filename=main.py ext=.py |>