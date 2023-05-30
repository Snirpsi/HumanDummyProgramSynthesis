#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words. """    
    while True:
        words = input("Enter a word: ").split()
        if words:
            print(" ".join(words))
        else:
            break

<|/ file ext=.py source=github |>