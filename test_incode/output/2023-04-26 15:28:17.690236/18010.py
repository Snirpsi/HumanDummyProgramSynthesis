#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or opens fruits. """    
    
    ports = list( map( int, open( "/dev/tty