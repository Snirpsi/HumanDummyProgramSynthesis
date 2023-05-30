#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or iterates over a list of numbers. """    
    while True:
        ports = list( range( 1, 65535 ) )
        
        for port in ports:
            print( '