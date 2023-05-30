#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and iterates over a list of words. """    
    
    ports = list( map( lambda port: port.strip(), sys.argv[1:] ) )
    
    for port in ports:
        
        if port in list( map( lambda port: port.strip(), sys.argv[1:] ) ):
            
            