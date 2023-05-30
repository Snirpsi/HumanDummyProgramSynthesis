#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and prints a port. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print('Port {} is open'.format(port))
        
    
