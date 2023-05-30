#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and iterates over fruits. """    
    words = read_words()
    fruits = read_fruits()
    for fruit in fruits:
        if fruit in words:
            print(words[fruit])
        else:
            print("No such fruit: " + fruit)

<|/ file source=github ext=.py |>