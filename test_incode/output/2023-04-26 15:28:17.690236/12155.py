#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    if len(words) == 0:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print('%s -> %s' % (word, word