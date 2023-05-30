#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or returns words. """    
    while True:
        port = str(input('Enter a port number: '))
        if port == '':
            break
        else:
            print(port)

<|/ file ext=.py |>