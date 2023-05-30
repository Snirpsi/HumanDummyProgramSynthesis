#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers and converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers.txt>" % sys.argv[0])
        sys.exit()
    
    numbers = open(sys.argv[1]).read().splitlines()
    
    numbers = [int(n) for n in numbers]
    
    numbers_cleaned = []
    
    for n in numbers:
        if n not in numbers_cleaned:
            numbers_cleaned.append(n)
    
    print(numbers_cleaned)
    
