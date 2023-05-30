#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words and opens all ports. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    ports = openports(words)
    
    for port in ports:
        
        