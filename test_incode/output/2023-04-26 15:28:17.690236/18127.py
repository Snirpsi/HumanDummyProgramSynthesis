#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = [x.strip() for x in sys.argv[1].split(',')]
    else:
        words = ['hello', 'world']
    
    words = [x.lower() for x in words]
    
    