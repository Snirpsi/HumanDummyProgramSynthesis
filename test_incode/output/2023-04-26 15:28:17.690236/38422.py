#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and enumerates words. """    
    while True:
        port = input('Enter a port number: ')
        words = [word.upper() for word in port.split()]
        print('\n'.join(words))
