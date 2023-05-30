#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    numbers = map(int, word