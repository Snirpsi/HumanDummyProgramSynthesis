#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or returns numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [words|numbers]' % sys.argv[0])
        sys.exit()
    
    mode = sys.argv[1]
    
    if mode == 'words':
        words = sys.argv[2:]
        
        print('\n'.join(words))
    elif mode == 'numbers':
        numbers = sys.argv[2:]
        
        print('\n'.join(map(str, numbers)))
    else:
        print('Usage: %s [words|numbers]' % sys.argv[0])
        sys.exit()
    
