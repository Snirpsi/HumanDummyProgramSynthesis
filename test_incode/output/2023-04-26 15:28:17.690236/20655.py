#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers or returns words. """    
    import sys
    
    numbers = sys.argv[1]
    words = sys.argv[2]
    
    numbers = numbers.split()
    words = words.split()
    
    numbers = [int(n) for n in numbers]
    words = [w.lower() for w in words]
    
    print(numbers)
    print(words)
    
