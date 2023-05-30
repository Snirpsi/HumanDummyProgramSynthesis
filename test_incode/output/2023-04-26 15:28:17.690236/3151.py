#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: %s <words> <numbers>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    numbers = sys.argv[2].split()
    
    numbers_set = set(numbers)
    
    numbers_set = numbers_set - set(words)
    
    numbers_set = list(numbers_set)
    
    numbers_set = sorted(numbers_set)
    
    numbers_set = map(int, numbers_set)
    
    numbers_set = list(numbers_set)
    
    numbers_set = sorted(numbers_set)
    
    numbers_set = map(str, numbers_set)
    
    numbers_set = ' '.join(numbers_set)
    
    print("Removed %d words and %d numbers from %s" % (len(words), len(numbers_set), sys.argv[0]))
    
    print(numbers_set)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    