#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and converts a port. """    
    ports = range(1,65535)
    while True:
        port = str(input('Enter a port number: '))
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        else:
            print('Opening port ' + str(port))
            