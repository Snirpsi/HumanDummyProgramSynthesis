#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1].split()
    
    words = [w for w in words if w]
    
    if len(words) == 0:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    numbers = map(int, sys.argv[2:])
    
    numbers = list(numbers)
    
    numbers = map(lambda x: x*numbers[0], numbers)
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(x), numbers)
    
    numbers = map(lambda x: str(