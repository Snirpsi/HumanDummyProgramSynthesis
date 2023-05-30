#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    port = 1
    
    while True:
        
        port = port + 1
        
        if port > 65535:
            port = 65535
        
        print('Port {}: {}'.format(port, 