#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or returns a port. """    
    
    port = 0
    
    while True:
        port = raw_input('Port: ')
        
        if port == 'exit':
            break
        
        