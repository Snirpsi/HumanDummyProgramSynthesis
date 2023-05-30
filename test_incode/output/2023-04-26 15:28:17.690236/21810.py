#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = [word.strip() for word in sys.argv[1].split(',')]
    else:
        words = sys.argv[1].split(',')
    
    for word in words:
        print(word)
    
