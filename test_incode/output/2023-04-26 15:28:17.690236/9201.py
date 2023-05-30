#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and returns fruits. """    
    ports = list( map( int, input().split() ) )
    fruits = list( map( int, input().split() ) )
    
    fruits.remove( ports[0] )
    fruits.remove( ports[1] )
    
    print( 