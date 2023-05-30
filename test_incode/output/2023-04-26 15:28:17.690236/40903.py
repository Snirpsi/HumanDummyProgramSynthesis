#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and converts fruits. """    
    
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
    
    print('\n'.join(words))
    print('\n'.join(