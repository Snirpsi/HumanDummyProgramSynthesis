#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and removes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        
        if port == -1:
            print('Invalid port number')
            continue
        
        