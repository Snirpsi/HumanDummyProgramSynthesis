#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports. """    
    
    ports = list( map( int, sys.argv[1:] ) )
    
    for port in ports:
        
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.bind( ( '127.0.0.1', port ) )
        sock.listen( 1 )
        
        while True:
            
            client, addr = sock.accept()
            
            client.send( b'\n' )
            
            client.close()
            
            sock.close()
            
