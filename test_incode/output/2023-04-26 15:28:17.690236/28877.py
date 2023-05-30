#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or enumerates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words|port]" % sys.argv[0])
        sys.exit(0)
    
    words = False
    port = False
    
    if len(sys.argv) == 2:
        if sys.argv[1] == "words":
            words = True
        else:
            port = True
    
    if words:
        words = sys.argv[1].split("|")
        
    port = int(sys.argv[2])
    
    enumerateWords(words)
    
    if port:
        enumeratePort(port)
        
    else:
        print("Usage: %s [words|port]" % sys.argv[0])
        sys.exit(0)
        
