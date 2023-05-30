#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import sys
    
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers = sorted(numbers)
    
    print(numbers)
    
    
