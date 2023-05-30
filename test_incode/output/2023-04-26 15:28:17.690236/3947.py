#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or converts numbers. """    
    while True:
        port = input('Enter a port number: ')
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
        else:
            print('Converting port number {} to {}'.format(port, 