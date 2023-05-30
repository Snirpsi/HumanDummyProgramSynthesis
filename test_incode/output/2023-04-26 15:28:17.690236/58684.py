#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words or iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    while True:
        
        words.append(sys.stdin.readline())
        
        if len(words) == port:
            
            print(" ".join(words))
            
            words = []
            
        else:
            
            