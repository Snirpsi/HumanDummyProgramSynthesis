#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or iterates over fruits. """    
    
    port = 0
    while True:
        port = port + 1
        
        # Open a port if port is unavailable
        if port > 65535:
            port = 0
            
        # Open a port if port is available
        else:
            