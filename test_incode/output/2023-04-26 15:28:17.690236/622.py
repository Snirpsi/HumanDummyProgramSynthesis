#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and opens all ports. """    
    
    ports = []
    
    for word in words:
        
        ports.append(Port(word))
        
    ports.