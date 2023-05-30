#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and removes a port. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    for word in words:
        sys.stdout.write(word)
        sys.stdout.write('\n')
    
    sys.stdout.write('\n')
    
    
