#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or prints a list of numbers. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        