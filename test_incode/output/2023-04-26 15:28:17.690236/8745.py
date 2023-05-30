#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or enumerates all ports. """    
    while True:
        try:
            port = int(input('Enter a port number: '))
        except ValueError:
            print('That is not a valid port')
        else:
            print('Converting port {} to {}'.format(port, 