#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and iterates over words. """    
    
    port = '/dev/ttyUSB0'
    
    while True:
        words = port.read().split()
        
        for word in words:
            print(word)
        
        port.close()
        
