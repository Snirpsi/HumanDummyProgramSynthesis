#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or returns all ports. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        print('Port: ', port)
        
