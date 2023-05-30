#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        numbers = map(int, sys.argv[1:])
        
        numbers_sum = reduce(lambda x,y: x*y, numbers)
        
        print('The sum of the numbers: ', numbers_sum)
        
    else:
        print('Usage: python 