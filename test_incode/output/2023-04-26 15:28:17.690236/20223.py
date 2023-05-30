#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or enumerates a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'a'
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    print(' '.join(map(str, numbers)))
    
