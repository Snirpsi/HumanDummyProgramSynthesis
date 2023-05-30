#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or returns a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        
        print('Adding port {}...'.format(port))
        
        