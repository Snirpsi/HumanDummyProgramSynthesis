#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    for arg in sys.argv[2:]:
        words.append(arg)
    
    words.sort()
    
    port2 = port * len(words)
    
    print('The port multiplied by %d words is: %d.' % (len(words), port2))
    
