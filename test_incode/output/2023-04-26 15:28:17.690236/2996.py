#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words.sort()
    
    words = [str(word) for word in words]
    
    word