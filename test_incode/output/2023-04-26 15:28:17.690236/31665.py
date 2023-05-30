#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and enumerates a port. """    
    
    ports = range(10000)
    
    while True:
        for port in ports:
            print('Enumerating port {}'.format(port))
            
            