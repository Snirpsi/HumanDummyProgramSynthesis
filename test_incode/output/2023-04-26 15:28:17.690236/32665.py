#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = [int(x) for x in numbers]
    
    numbers_removed = [x for x in numbers if x not in numbers]
    
    print('Removed %d numbers' % len(numbers_removed))
    
    for number in numbers_removed:
        print('Removed %d' % number)
    
