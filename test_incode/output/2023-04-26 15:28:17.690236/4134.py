#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or prints user input. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('Goodbye!')
            break
        else:
            print('