#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or returns a list of words. """    
    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == 'q':
            break
    
    print("\n".join(words))

<|/ file source=github ext=.py |>