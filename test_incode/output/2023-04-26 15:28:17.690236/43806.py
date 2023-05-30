#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or enumerates all ports. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('No port number given.')
        else:
            print('Found port number:', port)
            
