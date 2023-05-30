#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and multiplyes a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
    
    words = words[:port]
    
    words.sort()
    
    for word in words:
        print(word, end='')
    
