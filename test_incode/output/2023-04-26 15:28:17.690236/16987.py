#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and returns a port. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('