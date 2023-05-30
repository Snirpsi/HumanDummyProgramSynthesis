#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
        
    words.sort()
    
    sys.stdout.write('\n'.join(words))
    
