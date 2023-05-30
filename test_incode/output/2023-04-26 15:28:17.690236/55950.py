#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or removes a list of numbers. """    
    ports = list( map( int, sys.argv[1:] ) )
    ports.remove( 8080 )
    ports.remove( 8081 )
    ports.remove( 8082 )
    ports.remove( 8083 )
    ports.remove( 8084 )
    ports.remove( 8085 )
    ports.remove( 8086 )
    ports.remove( 8087 )
    ports.remove( 8088 )
    ports.remove( 8089 )
    ports.remove( 8090 )
    ports.remove( 8091 )
    ports.remove( 8092 )
    ports.remove( 8093 )
    ports.remove( 8094