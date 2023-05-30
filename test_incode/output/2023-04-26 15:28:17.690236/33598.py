#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            if arg.startswith('-'):
                words.append(arg)
            else:
                words.append(arg)
    else:
        words = ['help']
    
    print(words)
    
