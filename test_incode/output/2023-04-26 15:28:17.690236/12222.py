#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and enumerates all ports. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        
        ports = enumeratePorts(word)
        
        for port in ports:
            
            print(port[0], port[1])
            
