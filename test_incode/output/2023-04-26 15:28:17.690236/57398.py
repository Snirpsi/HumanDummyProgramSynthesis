#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or iterates over a list of words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
        else:
            break
    
    words = list(set(words))
    
    words.sort()
    
    sys.stdout.write(' '.join(words))
    
    sys.stdout.flush()
    
