#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or iterates over user input. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        else:
            print('Opening port ' + port)
            open