#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['apple', 'banana', 'cherry']
    
    words.sort()
    
    print('\n'.join(words))
    
