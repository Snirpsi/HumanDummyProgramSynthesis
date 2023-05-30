#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and converts a port. """    
    while True:
        port = int(input('Enter a port number: '))
        port = str(port)
        
        if port == '':
            print('Invalid port number')
            continue
        
        