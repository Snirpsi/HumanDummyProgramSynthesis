#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and iterates over numbers. """    
    
    port = 1
    
    while True:
        
        print('Port {} is open'.format(port))
        
        port += 1
        
        if port > 65535:
            
            print('Port {} is close