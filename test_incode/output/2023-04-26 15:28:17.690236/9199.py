#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or iterates over a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['a', 'b', 'c']
    
    numbers = [int(x) for x in words]
    
    for number in numbers:
        print(number * number)
    
