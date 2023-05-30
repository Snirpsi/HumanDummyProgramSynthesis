#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or multiplyes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == 0: break
        if port % 2 == 0:
            print('The port number is', port, 'multiplied by 2')
        else:
            print('The port number is', port, 'multiplied by 3')
