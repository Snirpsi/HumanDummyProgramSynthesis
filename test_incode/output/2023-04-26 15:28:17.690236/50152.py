#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or returns a port. """    
    
    port = 0
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
    print('The port number is', port)
    
