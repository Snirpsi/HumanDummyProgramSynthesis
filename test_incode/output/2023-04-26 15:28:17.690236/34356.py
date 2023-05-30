#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 0
        
    words = []
    
    if port > 0:
        words.append("port")
        
    if port < 0:
        words.append("ports")
        
    
    for word in words:
        print("%s\t%s" % (word, port