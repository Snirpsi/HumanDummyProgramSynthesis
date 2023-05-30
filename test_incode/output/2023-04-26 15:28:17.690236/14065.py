#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and enumerates all ports. """    
    ports = list( map( int, open('/proc/self/