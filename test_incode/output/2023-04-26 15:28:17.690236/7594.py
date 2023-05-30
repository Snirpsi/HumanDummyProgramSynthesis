#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words.txt>' % sys.argv[0])
        sys.exit(1)
    
    words = open(sys.argv[1]).read().splitlines()
    
    for word in words:
        print('%s: %s' % (word, 