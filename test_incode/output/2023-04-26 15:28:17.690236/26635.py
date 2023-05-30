#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports. """    
    ports = list( enumerate( socket.getservbyname( "http", "https" ) ) )
    for port in ports:
        print( port[1], port[0] )
    
