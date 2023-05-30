#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word)

<|/ file source=github dstars=0 filename=main.py |>