#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or enumerates a list of words. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    if port > 65535:
        sys.exit('Error: port number out of range')
    
    words.append(str(port))
    
    for i in range(1, port+1):
        words.append(str(i))
        
    words.sort()
    
    for word in words:
        print(word)
    
