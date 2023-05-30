#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    numbers_sum = reduce(lambda x, y: x*y, numbers)
    
    print("The sum of the numbers is {}".format(numbers_sum))
    
