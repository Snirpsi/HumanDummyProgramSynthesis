#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    print('\n'.join(words))
    
