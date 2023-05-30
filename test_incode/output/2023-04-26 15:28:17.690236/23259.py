#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or converts a list of words. """    
    while True:
        words = input('Enter a word: ')
        if words:
            words = words.split()
            words = [int(word) for word in words]
            print(words)
        else:
            break

<|/ file filename=main.py |>