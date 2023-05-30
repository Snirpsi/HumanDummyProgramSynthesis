#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = [sys.argv[1], sys.argv[2]]
    else:
        words = ['words', 'word']
    
    words.sort()
    
    for word in words:
        print('%s %s' % (word, 