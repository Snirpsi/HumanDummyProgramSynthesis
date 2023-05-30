#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and adds numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = [int(x) for x in numbers]
    
    numbers = sum(numbers)
    
    print('The total is %d' % numbers)
    
