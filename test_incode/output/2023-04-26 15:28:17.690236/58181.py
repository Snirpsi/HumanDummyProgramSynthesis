#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or calculates all ports. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
    
    words = []
    
    for word in sys.stdin:
        words.append(word)
    
    words = list(set(words))
    
    words.sort()
    
    ports = []
    
    for word in words:
        ports.append(port * word)
    
    print(" ".join(ports))
    
