#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and calculates a port. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    port = 0
    
    while True:
        
        word = words[port]
        
        port += 1
        
        if port == len(words):
            port = 0
            
        print('{} is {} 