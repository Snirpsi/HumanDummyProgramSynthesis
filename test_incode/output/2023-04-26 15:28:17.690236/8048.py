#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = map(int, sys.argv[1:])
        print('\n'.join(map(str, numbers)))
    else:
        print('Usage: python 