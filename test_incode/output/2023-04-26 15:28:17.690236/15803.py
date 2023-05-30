#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or opens words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word)
    
<|/ file source=github ext=.py |>