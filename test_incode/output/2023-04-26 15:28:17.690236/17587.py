#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and adds a list of words. """    
    
    port = '/dev/ttyUSB0'
    
    words = list()
    
    while True:
        words.append( port )
        
        port = open( port, 'r' ).read()
        
        if port == '':
            break
        
        words = words + 