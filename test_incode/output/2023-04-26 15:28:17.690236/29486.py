#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports. """    
    while True:
        port = input('Enter a port:')
        try:
            port = int(port)
        except ValueError:
            print('Invalid port')
            continue
        
        