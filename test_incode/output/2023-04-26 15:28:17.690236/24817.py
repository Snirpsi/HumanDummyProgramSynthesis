#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and converts a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    sys.stdout.write("\n".join(words))
    
    sys.stdout.flush()
    
