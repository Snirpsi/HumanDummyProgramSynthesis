#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    numbers = [int(n) for n in sys.argv[1:]]
    
    for n in numbers:
        print(n)
        
