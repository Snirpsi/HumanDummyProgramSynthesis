#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or opens a port. """    
    port = None
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        