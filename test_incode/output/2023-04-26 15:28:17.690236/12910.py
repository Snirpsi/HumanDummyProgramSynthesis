#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or enumerates numbers. """    
    ports = [
        port for port in range(1, 65535)
        if port % 2 == 0
    ]
    
    for port in ports:
        print('Found port {}'.format(port))
    
