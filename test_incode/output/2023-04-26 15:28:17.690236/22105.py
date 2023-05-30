#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or enumerates numbers. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port < 1 or port > 65535:
            print('Port number must be between 1 and 65535.')
        else:
            print('Enumerating port number %s...' % port)
            
            
