#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or returns words. """    
    while True:
        line = input('> ')
        if line == 'exit':
            break
        else:
            print(line)

<|/ file filename=main.py dstars=0 |>