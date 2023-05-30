#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit(-1)
    
    numbers = []
    
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            numbers.extend(map(int, f.read().splitlines()))
    
    numbers = list(set(numbers))
    numbers.sort()
    
    for number in numbers:
        print("%d\t%s" % (number, number