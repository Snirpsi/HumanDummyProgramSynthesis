#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or stores a port. """    
    port = 1
    while True:
        port = input('Enter a port number: ')
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
        else:
            break
    print('The port number is', port)
    
