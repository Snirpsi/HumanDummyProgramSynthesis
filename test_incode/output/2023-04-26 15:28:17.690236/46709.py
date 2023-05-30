#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s number" % sys.argv[0])
        sys.exit()
    
    number = int(sys.argv[1])
    
    if number < 1:
        print("Usage: %s number" % sys.argv[0])
        sys.exit()
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    numbers_removed = [n for n in numbers if n not in numbers]
    
    print(numbers_removed)
    
