#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and converts words. """    
    
    port = '/dev/ttyUSB0'
    
    while True:
        
        words = port.split()
        
        for word in words:
            print(word)
            
        time.sleep(1)
        
