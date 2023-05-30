#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and calculates a port. """    
    
    port = 0
    while True:
        port = port + 1
        
        if port > 65535:
            port = port%65535
        
        print('Port #' + str(port) + ' is ' + str(