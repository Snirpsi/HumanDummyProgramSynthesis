#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and stores all ports. """    
    
    import sys
    
    words = sys.argv[1:]
    
    ports = []
    
    for word in words:
        
        ports.append(word)
    
    for port in ports:
        
        print(port)
        
