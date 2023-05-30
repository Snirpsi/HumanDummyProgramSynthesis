#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or multiplyes numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port % 2 == 0:
            print(port)
        else:
            print(port * 2)
