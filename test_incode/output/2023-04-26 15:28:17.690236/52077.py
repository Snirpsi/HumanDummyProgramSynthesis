#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port or adds numbers. """    
    
    port = 0
    
    while True:
        port = port + 1
        
        if port > 65535:
            port = port - 65535
            
        print('Port {}: {}'.format(port, 