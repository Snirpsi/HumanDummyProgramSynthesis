#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or opens words. """    
    while True:
        port = input('Enter a port number: ')
        port = int(port)
        if port > 65535:
            print('Error: port number must be less than 65535')
        else:
            