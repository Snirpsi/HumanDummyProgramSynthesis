#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words or removes user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            print(word)
            
<|/ file source=github ext=.py |>