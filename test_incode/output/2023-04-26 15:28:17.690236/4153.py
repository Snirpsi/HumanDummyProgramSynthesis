#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and enumerates a list of words. """    
    
    words = []
    
    while True:
        
        ports = range(10000, 20000, 100)
        
        for port in ports:
            
            words.append(str(port