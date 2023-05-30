#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or returns a port. """    
    
    port = 5000
    
    while True:
        
        words = words_in_port(port)
        
        if words:
            print(words)
            
        port += 1
        
        if port == 