#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or enumerates all ports. """    
    
    ports = range(1023)
    
    ports_iter = iter(ports)
    
    ports_iter = ports_iter.