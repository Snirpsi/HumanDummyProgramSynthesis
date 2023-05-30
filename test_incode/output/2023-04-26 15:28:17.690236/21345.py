#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or iterates over numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        exit(1)
    
    numbers = sys.argv[1:]
    
    numbers_iter = iter(numbers)
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__iter__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
        print(number * 2)
    
    numbers_iter = numbers.__next__()
    
    for number in numbers_iter:
