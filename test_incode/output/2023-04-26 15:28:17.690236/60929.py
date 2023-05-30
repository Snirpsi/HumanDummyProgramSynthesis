#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and returns fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ('apple', 'banana', 'cherry')
    
    fruits = ''
    
    for word in words:
        fruit