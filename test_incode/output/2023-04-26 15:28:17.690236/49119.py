#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and enumerates words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(str(i))
        
    while True:
        for word in words:
            print(word)
        
        