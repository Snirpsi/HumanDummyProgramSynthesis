#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit(1)
    
    numbers = sys.argv[1:]
    
    numbers = [int(i) for i in numbers]
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    print(numbers)
    
    
