#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or prints fruits. """    
    
    while True:
        
        print('Port: ')
        
        port = int(input('Port: '))
        
        if port == -1:
            break
        
        print('Fruits: ')
        
        fruits = 