#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and opens all ports. """    
    while True:
        port = input('Enter a port number: ')
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
        else:
            