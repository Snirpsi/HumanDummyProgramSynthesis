#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports and calculates words. """    
    
    ports = list( map( int, open('/proc/net/tcp').read().splitlines() ) )
    
    for port in ports:
        words = port.split('/')
        
        for word in words:
            print(word, end=' ')
            
        print('')
        
