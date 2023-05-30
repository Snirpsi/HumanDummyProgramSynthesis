#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or iterates over all ports. """    
    
    ports = range(5000, 6000)
    
    ports_iter = iter(ports)
    
    ports_iter = ports_iter.