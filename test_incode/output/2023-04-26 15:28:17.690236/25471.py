#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or opens words. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        # Open a port and print its contents
        open