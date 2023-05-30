#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports and removes all ports. """    
    ports = list( map( int, open('/proc/net/tcp').read().split('\n') ) )
    for port in ports:
        