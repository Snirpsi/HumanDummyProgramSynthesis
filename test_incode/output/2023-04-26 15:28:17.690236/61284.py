#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or enumerates a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    words = []
    
    words.append(sys.argv[1])
    
    for word in sys.argv[2:]:
        words.append(word)
    
    words.sort()
    
    for word in words:
        print('%s * %s' % (word, port