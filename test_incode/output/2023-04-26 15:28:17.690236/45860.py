#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and converts user input. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    sys.stdout.write('\n'.join(words))
    sys.stdout.flush()
    
