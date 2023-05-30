#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    sys.stdout.write("\n".join(words))
    sys.stdout.flush()
    
