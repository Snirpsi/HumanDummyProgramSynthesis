#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and calculates words. """    
    
    port = '/dev/ttyUSB0'
    
    while True:
        
        words = port.count(' ')
        
        print('Port: ', port)
        print('Words: ', words)
        
        port = input('Enter new port