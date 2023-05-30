#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <file> [<file> ...]' % sys.argv[0])
        sys.exit()
    
    numbers = []
    for filename in sys.argv[1:]:
        with open(filename) as f:
            numbers.extend(map(int, f.read().split()))
    
    numbers = list(map(lambda x: x * x, numbers))
    
    print('\n'.join(map(str, numbers)))

<|/ file source=github ext=.py |>