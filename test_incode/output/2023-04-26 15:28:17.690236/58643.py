#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports. """    
    
    ports = []
    while True:
        ports.append( int( input('Enter a port number: ') ) )
        
        if ports[-1] == 255:
            break
            
    print('\n'.join(map(str, ports)))
    
