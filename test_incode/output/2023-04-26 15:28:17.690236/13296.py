#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and opens all ports. """    
    
    words = ['hello', 'world', 'python', 'is', 'fun']
    
    ports = []
    
    for word in words:
        
        ports.append( open( word, 