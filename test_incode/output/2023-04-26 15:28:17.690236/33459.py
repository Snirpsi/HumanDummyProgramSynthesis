#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    for word in words:
        print(word * 2)
    
