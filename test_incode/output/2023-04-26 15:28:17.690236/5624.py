#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and enumerates a port. """    
    import sys
    words = []
    ports = []
    for arg in sys.argv[1:]:
        words.append(arg)
        ports.append(int(arg))
    
    words.sort()
    ports.sort()
    
    ports = ports[::-1]
    
    for word in words:
        print("%d\t%s" % (ports.index(word), word))
    
