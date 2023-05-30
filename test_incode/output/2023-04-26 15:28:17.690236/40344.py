#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or adds a port. """    
    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        else:
            print('Port number 