#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    words = [w.upper() for w in words]
    
    print('\n'.join(words))
    
