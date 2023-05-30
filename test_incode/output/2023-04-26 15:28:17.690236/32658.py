#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or adds words. """    
    import sys
    port = sys.argv[1]
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    words.sort()
    print('\n'.join(words))
