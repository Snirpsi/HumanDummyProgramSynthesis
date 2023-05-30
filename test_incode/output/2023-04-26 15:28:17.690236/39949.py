#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or multiplyes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port > 0 and port < 65535:
            print('The port is {}'.format(port))
        else:
            print('Invalid port number')
