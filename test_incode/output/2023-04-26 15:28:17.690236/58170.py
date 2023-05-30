#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or prints all ports. """    
    ports = list( map( int, sys.argv[1:] ) )
    ports = ports + list(range( 65536, 65536 + len(ports) ) )
    
    httpd = 