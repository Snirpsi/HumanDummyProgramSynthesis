#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and removes a list of words. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    words.sort()
    
    words = [word for word in words if word not in sys.argv[2:]]
    
    print(" ".join(words))
    
