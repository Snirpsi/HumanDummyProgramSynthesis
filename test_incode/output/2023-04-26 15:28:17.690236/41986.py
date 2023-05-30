#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or stores a port. """    
    port = int(input('Enter a port: '))
    
    if port == -1:
        print('Invalid port')
    else:
        print('Opening port {}'.format(port))
        
        