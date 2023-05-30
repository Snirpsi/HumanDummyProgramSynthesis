#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words|numbers>' % sys.argv[0])
        sys.exit(1)
    
    if sys.argv[1] == 'words':
        words = sys.argv[2:]
        print('\n'.join(words))
    elif sys.argv[1] == 'numbers':
        numbers = sys.argv[2:]
        print('\n'.join(map(str, numbers)))
    else:
        print('Usage: %s <words|numbers>' % sys.argv[0])
        sys.exit(1)
    
