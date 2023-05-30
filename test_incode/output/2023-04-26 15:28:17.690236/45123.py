#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and returns a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.extend(arg.split())
    
    words = list(set(words))
    
    words = list(map(lambda x: x*2, words))
    
    print('\n'.join(words))

