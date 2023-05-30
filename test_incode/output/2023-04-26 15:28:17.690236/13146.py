#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_iter = iter(numbers)
    
    numbers_iter = map(int, numbers_iter)
    
    numbers_iter = zip(numbers_iter, numbers_iter)
    
    numbers_iter = map(operator.mul, numbers_iter, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_iter = map(str, numbers_iter)
    
    numbers_