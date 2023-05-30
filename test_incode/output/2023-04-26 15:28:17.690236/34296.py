#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = enumerate()
    
    for port in ports:
        print('Port {} is {}'.format(port, ports[port]))
        
