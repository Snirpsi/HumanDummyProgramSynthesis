#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or enumerates a port. """    
    
    port = int(input('Enter a port number: '))
    
    if port > 0 and port < 65535:
        print('Port number 