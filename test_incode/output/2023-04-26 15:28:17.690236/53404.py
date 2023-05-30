#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    numbers = map(int, open(filename).readlines())
    
    numbers = map(lambda x: x*x, numbers)
    
    print(numbers)
    
