#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'hello'
    
    print('%s is %s' % (word, word*word))
    
