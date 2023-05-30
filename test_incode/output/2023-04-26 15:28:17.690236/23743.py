#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports and prints all ports. """    
    
    ports = range(1,65535)
    
    while True:
        ports_str = ','.join(ports)
        print('Ports: %s' % ports_str)
        
        ports = ports[ports.index