#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or enumerates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'enumerate':
            enumerate_words()
        elif word == 'list':
            enumerate_words()
        else:
            print('Usage: %s enumerate|list' % sys.argv[0])
    else:
        print('Usage: %s enumerate|list' % sys.argv[0])
    
