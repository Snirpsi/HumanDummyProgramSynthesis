#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    words = open(filename).read().split()
    
    words = [str(word) for word in words]
    
    numbers = open(filename).read().split()
    
    numbers = [int(number) for number in numbers]
    
    numbers = [number * 2 for number in numbers]
    
    numbers = [number + 2 for number in numbers]
    
    numbers = [number - 2 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number + 3 for number in numbers]
    
    numbers = [number - 2 for number in numbers]
    
    numbers = [number + 2 for number in numbers]
    
    numbers = [number - 1 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 3 for number in numbers]
    
    numbers = [number + 1 for number in numbers]
    
    numbers = [number - 1 for number in numbers]
    
    numbers = [number + 1 for number 