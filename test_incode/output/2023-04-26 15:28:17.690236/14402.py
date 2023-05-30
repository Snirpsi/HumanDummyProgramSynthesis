#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or calculates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    numbers = [int(w) for w in words]
    
    numbers = list(filter(lambda x: x is not None, numbers))
    
    numbers = list(map(lambda x: x * 10, numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
    
    numbers = list(map(lambda x: str(x), numbers))
