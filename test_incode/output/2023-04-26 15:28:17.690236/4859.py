#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports. """    
    ports = list( map( int, open('/proc/net/tcp').read().split('\n') ) )
    
    print('\n'.join( map( '{:02x}'.format( port ), ports ) ))

<|/ file ext=.py source=github |>