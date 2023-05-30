#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or removes all ports. """    
    import sys
    
    ports = [int(i) for i in sys.argv[1:]]
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    words = list(set(words))
    
    for port in ports:
        words = [w for w in words if port in w]
    
    for word in words:
        print(word)
    
