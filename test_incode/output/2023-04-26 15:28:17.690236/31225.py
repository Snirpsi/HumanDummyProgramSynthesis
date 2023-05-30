#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = list(filter(None, words))
    
    words.sort()
    
    words = [str(word) for word in words]
    
    print('\n'.join(words))
    
