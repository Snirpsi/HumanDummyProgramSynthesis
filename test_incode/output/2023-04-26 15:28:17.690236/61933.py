#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or calculates a port. """    
    while True:
        port = int(input('Enter a port number: '))
        print('The port number is', port)
        if port > 0 and port < 65535:
            print('The port number is', port)
        else:
            print('The port number is', port, '