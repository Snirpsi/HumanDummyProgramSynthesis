#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    import sys
    port = sys.argv[1]
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    sys.stdout.write('\n'.join(words))
    sys.stdout.flush()
    
