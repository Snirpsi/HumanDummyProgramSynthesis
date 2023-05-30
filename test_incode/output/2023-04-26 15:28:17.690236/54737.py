#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    words = [word.capitalize() for word in words]
    
    sys.stdout.write(' '.join(words))
    
