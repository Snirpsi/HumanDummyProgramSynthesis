#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and calculates a port. """    
    
    port = 0
    
    while True:
        port = port + 1
        
        print("Port #" + str(port))
        
        