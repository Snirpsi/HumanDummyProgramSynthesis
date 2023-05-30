#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    print('\n'.join(words))
    
