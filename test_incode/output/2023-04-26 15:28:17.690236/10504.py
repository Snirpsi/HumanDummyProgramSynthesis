#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python enumerate.py <words>')
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    for word in words:
        print('%s: %s' % (word, 