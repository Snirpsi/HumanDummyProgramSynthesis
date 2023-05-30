#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and multiplyes all ports. """    
    while True:
        port = input('Enter a port number: ')
        port = int(port)
        ports = port * port
        print('The port number is', ports)
        
