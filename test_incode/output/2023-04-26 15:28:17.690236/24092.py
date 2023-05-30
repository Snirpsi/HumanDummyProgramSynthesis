#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and converts a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        print('Converting port {} to {}'.format(port, 