#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    print('\n'.join(map(str, numbers)))

<|/ file source=github filename=