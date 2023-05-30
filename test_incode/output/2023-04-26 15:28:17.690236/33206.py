#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or multiplyes a list of words. """    
    while True:
        port = int(input('Enter a port: '))
        if port == -1:
            break
        else:
            print(port*