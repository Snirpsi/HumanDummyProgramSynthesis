#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: wordserver.py <words>')
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words = list(set(words))
    
    print('\n'.join(words))
    
