#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or enumerates a port. """    
    while True:
        port = input('Enter a port number: ')
        if port == 'exit':
            break
        else:
            print('\nPort', port, 'is', 