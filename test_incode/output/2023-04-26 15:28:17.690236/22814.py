#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or iterates over a list of words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    for word in words:
        
        ports = openports(word)
        
        for port in ports:
            
            