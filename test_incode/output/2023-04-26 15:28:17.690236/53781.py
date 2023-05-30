#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [w for w in words if len(w) > 0]
    
    numbers = map(int, words)
    
    product = reduce(lambda x,y: x*y, numbers)
    
    print('The product of %d numbers is %d.' % (len(numbers), product))
    
