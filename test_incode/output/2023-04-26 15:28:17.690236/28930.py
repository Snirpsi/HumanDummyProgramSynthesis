#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words.sort()
    
    print('\n'.join(words))
    
