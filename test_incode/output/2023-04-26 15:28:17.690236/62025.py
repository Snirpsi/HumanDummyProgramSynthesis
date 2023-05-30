#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or calculates a port. """    
    while True:
        port = input('Enter a port number: ')
        port = int(port)
        if port < 0 or port > 65535:
            print('Invalid port number')
        else:
            print('The port is %d' % port)
            break
