#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or calculates a list of words. """    
    
    port = int(input("Enter a port number: "))
    
    words = []
    
    while True:
        words.append(str(port))
        
        port += 1
        
        if port > 65535:
            port = 1
            
        if port == 65535:
            break
        
    print(" ".join(words))
    
    
