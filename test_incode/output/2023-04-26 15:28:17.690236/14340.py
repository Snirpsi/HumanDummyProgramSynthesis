#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports. """    
    ports = []
    
    ports.append( ('192.168.1.1', 80) )
    ports.append( ('192.168.1.2', 80) )
    ports.append( ('192.168.1.3', 80) )
    
    for port in ports:
        print( '{}: {}'.format( *port ) )
        
