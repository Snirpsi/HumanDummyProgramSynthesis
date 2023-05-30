#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or iterates over a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ports = []
    
    while True:
        ports.append(len(words))
        
        for word in words:
            print(word)
            
        words = []
        
        for port in ports:
            print(port)
            
        ports = []
        
