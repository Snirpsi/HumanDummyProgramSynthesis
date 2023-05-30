#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports and enumerates user input. """    
    while True:
        ports = enumerate_ports()
        print('\n'.join(ports))
        
