#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or prints a port. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        if arg == '--words':
            words = list(set(sys.argv[2:]))
        elif arg == '--port':
            port = sys.argv[2]
        else:
            words.append(arg)
    
    if len(words) == 0:
        print('Usage: %s [--words words] [--port port]' % sys.argv[0])
        sys.exit(1)
    
    port = int(port)
    
    for word in words:
        print('%s %s' % (word, port))
        
