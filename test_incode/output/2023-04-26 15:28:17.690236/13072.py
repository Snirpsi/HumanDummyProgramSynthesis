#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or returns a list of words. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    if len(ports) == 1: # single port
        
        words = []
        
        for port in ports:
            
            words.append(str(port))
            
        return words
    
    else: # multiple ports
        
        words = []
        
        for port in ports:
            
            words.append(str(port) + 