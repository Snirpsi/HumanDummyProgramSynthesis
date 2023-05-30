#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or prints a port. """    
    
    ports = enumerate()
    
    for port in ports:
        print('Port %s is %s.' % (port, ports[port]))
    
