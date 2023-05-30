#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    ports = []
    
    ports.append( ('TCP', ('0.0.0.0', 9000) ) )
    ports.append( ('TCP', ('0.0.0.0', 9001) ) )
    ports.append( ('TCP', ('0.0.0.0', 9002) ) )
    ports.append( ('TCP', ('0.0.0.0', 9003) ) )
    
    for port in ports:
        print( '\t', port[0], port[1] )
        
