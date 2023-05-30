#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or multiplyes a port. """    
    while True:
        port = int(input('Enter a port to multiply or 0 to quit: '))
        if port == 0:
            break
        else:
            print(port * 