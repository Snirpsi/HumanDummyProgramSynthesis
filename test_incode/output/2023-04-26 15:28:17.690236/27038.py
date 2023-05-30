#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    ports = list( map( int, sys.argv[1:] ) )
    
    for port in ports:
        
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        sock.bind( ( port, 0 ) )
        
        sock.close()
    
