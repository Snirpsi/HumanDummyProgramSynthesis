#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    for word in words:
        print('%s: %s' % (word, 