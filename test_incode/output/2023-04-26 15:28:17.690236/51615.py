#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports and iterates over words. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        words = port.split()
        
        for word in words:
            
            print(word)
            
