#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    if port == 0: # port 0 is reserved for system ports
        port = 0
    
    ports = enumerate()
    
    for port in ports:
        print('{:>2}'.format(port), end=' ')
    
    print('')
    
    if port > 0:
        print('Port {:d} is reserved for system ports.'.format(port))
    
    sys.exit()
    
