#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports. """    
    ports = list( map( int, sys.argv[1:] ) )
    for port in ports:
        print( port )
    
