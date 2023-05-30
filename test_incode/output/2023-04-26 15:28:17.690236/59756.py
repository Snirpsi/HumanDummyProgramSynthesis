#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and adds a port. """    
    while True:
        port = int(input('Enter a port number: '))
        print('Opening port {0}'.format(port))
        