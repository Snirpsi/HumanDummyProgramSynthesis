#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import os
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words.sort()
    
    sys.stdout.write(" ".join(map(lambda x: str(x), words)))
    
