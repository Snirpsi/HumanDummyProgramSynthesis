#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port. """    
    while True:
        port = input('Enter a port number: ')
        
        if port == 'q':
            break
        
        print('The port is {}'.format(port))
        
