#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or converts a port. """    
    while True:
        port = int(input('Enter a port: '))
        if port == -1:
            break
        
        