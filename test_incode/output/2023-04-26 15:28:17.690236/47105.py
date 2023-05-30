#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or prints a port. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        print('The port is {}'.format(port))
        
