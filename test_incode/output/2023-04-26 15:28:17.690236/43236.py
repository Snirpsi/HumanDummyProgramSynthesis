#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or iterates over fruits. """    
    
    port = 1
    
    while True:
        fruits = ['apple', 'banana', 'cherry']
        
        for fruit in fruits:
            print(fruit)
            
        port = port + 1
        
        if port > 65535:
            port = 1
            
