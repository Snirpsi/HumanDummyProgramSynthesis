#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and iterates over a port. """    
    
    port = 5000
    
    while True:
        words = words_from_port(port)
        
        for word in words:
            print(word)
            
        port = port + 1
        
        if port > 65535:
            port = 5000
            
