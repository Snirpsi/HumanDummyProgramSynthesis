#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    while True:
        port = int(input('Enter a port number: '))
        print('Server running on port ' + str(port))
