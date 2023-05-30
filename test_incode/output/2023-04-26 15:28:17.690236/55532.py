#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> <num>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    num = int(sys.argv[2])
    
    with open(filename) as f:
        content = f.readlines()
    
    numbers = [int(n) for n in content]
    
    numbers = [n * n for n in numbers]
    
    numbers = sum(numbers)
    
    print("The result is", numbers)
    
