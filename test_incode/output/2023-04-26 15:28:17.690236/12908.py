#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit(1)
    
    numbers = sys.argv[1:]
    
    numbers = [int(n) for n in numbers]
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(map(lambda x: x * 2, numbers))
    
    numbers = list(map(lambda x: x + 1, numbers))
    
    numbers = list(map(lambda x: x + 2, numbers))
    
    numbers = list(map(lambda x: x + 3, numbers))
    
    numbers = list(map(lambda x: x + 4, numbers))
    
    numbers = list(map(lambda x: x + 5, numbers))
    
    numbers = list(map(lambda x: x + 6, numbers))
    
    numbers = list(map(lambda x: x + 7, numbers))
    
    numbers = list(map(lambda x: x + 8, numbers))
    
    numbers = list(map(lambda x: x + 9, numbers))
    
    numbers = list(map(lambda x: x + 10, numbers))
    
    numbers = list(map(lambda x: x + 11, numbers))
    
    numbers = list(map(lambda x: x + 12, numbers))
    
    numbers = list(map(lambda x: x + 13, numbers))
    
    numbers = list(map(lambda x: x + 14, numbers))
    
    numbers = list(map(lambda x: x + 15, numbers))
    
    numbers = list(map(lambda x: x + 16, numbers))
    
    numbers = list(map(lambda x: x + 17, numbers))
    
    numbers = list(map(lambda x: x + 18, numbers))
    
    numbers = list(map(lambda x: x + 19, numbers))
    
    numbers = list(map(lambda x: x + 20, numbers))
    
    numbers = list(map(lambda x: x + 21, numbers))
    
    numbers = list(map(lambda x: x + 22, numbers))
    
    numbers = list(map(lambda x: x + 23, numbers))
    
    numbers = list(map(lambda x: x + 24, numbers))
    
    numbers = list(map(lambda x: x + 25, numbers))
    
    numbers = list(map(lambda x: x + 26, numbers))
    
    numbers = list(map(lambda x: x + 27, numbers))
    
    numbers = list(map(lambda x: x + 28, numbers))
    
    numbers = list(map(lambda x: x + 29, numbers))
    
    numbers = list(map(lambda x: x + 30, numbers))
    
    numbers = list(map(lambda x: x + 31, numbers))
    
    numbers = list(map(lambda x: x + 32, numbers))
    
    numbers = list(map(lambda x: x + 33, numbers))
    
    numbers = list(map(lambda x: x + 34, numbers))
    
    numbers = list(map(lambda x: x + 35, numbers))
    
    numbers = list(map(lambda x: x + 36, numbers))
    
    numbers = list(map(lambda x: x + 37, number