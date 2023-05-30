#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or opens a port. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        else:
            print('Opening port 