#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    words = [sys.argv[1], sys.argv[2]]
    
    words.extend(sys.argv[3:])
    
    words = ' '.join(words)
    
    print(' '.join(words))
    
