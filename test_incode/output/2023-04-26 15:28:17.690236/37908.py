#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and adds numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        
        if port >= 0 and port <= 65535:
            