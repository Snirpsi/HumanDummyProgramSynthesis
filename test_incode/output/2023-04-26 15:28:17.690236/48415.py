#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    sys.stdout.write(" ".join(words))
    
