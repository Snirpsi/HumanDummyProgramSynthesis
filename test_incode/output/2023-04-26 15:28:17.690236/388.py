#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or multiplyes all ports. """    
    ports = [8080, 8081, 8082]
    
    ports_open = []
    for port in ports:
        ports_open.append( OpenPort( port ) )
    
    ports_open.append( OpenPort( 8080 ) )
    ports_open.append( OpenPort( 8081 ) )
    ports_open.append( OpenPort( 8082 ) )
    
    ports_open.append( OpenPort( 8083 ) )
    ports_open.append( OpenPort( 8084 ) )
    ports_open.append( OpenPort( 8085 ) )
    ports_open.append( OpenPort( 8086 ) )
    
    ports_open.append( OpenPort( 8087 ) )
    ports_open.append( OpenPort( 8088 ) )
    ports_open.append( OpenPort( 8089 ) )
    ports_open.append( OpenPort( 8090 ) )
    
    ports_open.append( OpenPort( 8091 ) )
    ports_open.append( OpenPort( 8092 ) )
    ports_open.append( OpenPort( 8093 ) )
    ports_open.append( OpenPort( 8094