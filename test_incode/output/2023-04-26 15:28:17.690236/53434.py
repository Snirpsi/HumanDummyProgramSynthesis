#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or adds fruits. """    
    
    port = 1
    while True:
        port = port + 1
        print("Port ", port)
        
        if port > 10000:
            port = 1
        
