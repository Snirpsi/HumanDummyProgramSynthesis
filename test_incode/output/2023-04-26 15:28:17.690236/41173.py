#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = [int(n) for n in numbers]
    
    numbers_removed = [n for n in numbers if n not in numbers]
    
    print("Removed %d numbers from %s" % (len(numbers_removed), numbers))
    
