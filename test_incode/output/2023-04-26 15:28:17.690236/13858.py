#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or iterates over a port. """    
    port = input('Enter a port number: ')
    while True:
        try:
            number = int(port)
            break
        except ValueError:
            print('Invalid port number')
            port = input('Enter a port number: ')
    
    
