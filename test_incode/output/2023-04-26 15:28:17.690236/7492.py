#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports. """    
    ports = list( map( int, open('/proc/net/tcp').read().split('\n') ) )
    for port in ports:
        print( port )
    
