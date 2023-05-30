#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or returns a port. """    
    port = ''
    while True:
        try:
            port = input('Enter a port: '