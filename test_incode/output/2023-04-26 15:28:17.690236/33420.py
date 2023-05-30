#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or multiplyes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    
    numbers = list(map(lambda x: x * 2, numbers))
    
    print(numbers)
    
