#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits or enumerates all ports. """    
    
    ports = enumerate()
    
    while True:
        port = input('Enter a port number: ')
        if port in ports:
            print('Port {} is open'.format(port))
        else:
            print('Port {} is not open'.format(port))
            
