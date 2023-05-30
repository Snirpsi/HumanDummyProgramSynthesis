#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and removes a port. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        words = line.strip().split()
    
    words.sort()
    
    port = int(sys.argv[1])
    
    words = [word for word in words if word[:2] != '#' and word[:2] != '!' and word[:2] != '$']
    
    words = [word for word in words if word[:2] != '#' and word[:2] != '!' and word[:2] != '$' and word[:2] != '-']
    
    words = [word for word in words if word[:2] != '#' and word[:2] != '!' and word[:2] != '$' and word[:2] != '-' and word[:2] != '-']
    
    words = [word for word in words if word[:2] != '#' and word[:2] != '!' and word[:2] != '$' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-']
    
    words = [word for word in words if word[:2] != '#' and word[:2] != '!' and word[:2] != '$' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-']
    
    words = [word for word in words if word[:2] != '#' and word[:2] != '!' and word[:2] != '$' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[:2] != '-' and word[: