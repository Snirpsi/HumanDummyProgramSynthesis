#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or returns a list of words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        words = line.split()
        print(' '.join(words))

<|/ file filename=main.py source=github |>