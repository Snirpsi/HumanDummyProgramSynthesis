#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or returns fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [words]' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    fruits = convert_words(words)
    
    print('\n'.join(fruits))
    
