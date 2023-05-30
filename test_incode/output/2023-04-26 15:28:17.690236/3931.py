#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports and opens a port. """    
    ports = []
    while True:
        ports.append( int( input('Enter a port number: ') ) )
        open( ports[-1], '