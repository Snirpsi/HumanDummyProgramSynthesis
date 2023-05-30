#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = input('Enter a port number: ')
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        
        print('Converting port {} to {}'.format(port, 