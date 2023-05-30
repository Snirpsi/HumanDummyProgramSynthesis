#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or converts a port. """    
    while True:
        port = int(input('Enter a port: '))
        if port == -1:
            break
        
        if port == 0 or port == 65535:
            print('Converting port {} to hexadecimal...'.format(port))
            hex = hex