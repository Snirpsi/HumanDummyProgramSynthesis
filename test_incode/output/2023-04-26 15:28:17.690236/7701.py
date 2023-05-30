#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.sort()
    
    for word in words:
        print(word)
        
