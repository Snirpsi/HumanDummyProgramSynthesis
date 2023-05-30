#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and adds a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = words + line.split()
        
    words.sort()
    
    for word in words:
        print(word, end=' ')
        
        if port != 0 and port != port+1:
            print(