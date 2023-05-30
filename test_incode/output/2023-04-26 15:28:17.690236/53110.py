#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port and iterates over numbers. """    
    
    port = 0
    
    while True:
        port = port + 1
        
        if port > 65535:
            port = port - 65535
        
        print(port)
        
        if port == 65535:
            break
        
