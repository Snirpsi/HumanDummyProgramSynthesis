#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and enumerates fruits. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    fruits = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            fruits.append(line)
    
    words.sort()
    fruits.sort()
    
    sys.stdout.write('\n'.join(words))
    sys.stdout.write('\n')
    sys.stdout.write('\n'.join(