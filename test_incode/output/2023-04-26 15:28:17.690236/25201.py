#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or iterates over user input. """    
    
    import sys
    
    words = ['hello', 'world', '!']
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    sys.stdout.write(' '.join(words))
    sys.stdout.flush()
    
