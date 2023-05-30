#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 0
    
    words = []
    
    if port > 0:
        words.append("Port %d" % port)
    
    if port < 256:
        words.append("Port %d" % port)
        
    for word in words:
        print(word)
    
