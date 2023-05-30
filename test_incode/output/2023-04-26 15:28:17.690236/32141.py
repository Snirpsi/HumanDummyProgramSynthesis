#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or calculates numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port > 65535:
            print('Error: port number too large.')
        elif port < 1:
            print('Error: port number too small.')
        else:
            print('The port number is', port)
            
