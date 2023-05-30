#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or stores a list of words. """    
    
    ports = list( map( int, open( "/proc/net/tcp" ).read().split() ) )
    
    for port in ports:
        if port == 80:
            print( '