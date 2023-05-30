#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = list(map(int, numbers))
    
    numbers_removed = list(filter(lambda n: n not in numbers, numbers))
    
    print("Removed %d numbers" % len(numbers_removed))
    
    for n in numbers_removed:
        print("Removed %d" % n)
    
    
