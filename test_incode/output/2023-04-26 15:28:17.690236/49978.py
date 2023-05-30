#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words = words + arg.split(' ')
        
        for word in words:
            print(word)
    else:
        print('Usage: %s <words>' % sys.argv[0])
        print('')
        print('