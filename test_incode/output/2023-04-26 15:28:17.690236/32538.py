#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    numbers = []
    for number in words:
        numbers.append(int(number))
    
    numbers_iter = iter(numbers)
    
    numbers_iter *= 2
    
    numbers_iter *= 3
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 4
    
    numbers_iter *= 5
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 6
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 7
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 8
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 9
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 10
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 11
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 12
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 13
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 14
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 15
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 16
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 17
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 18
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 19
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 20
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 21
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 22
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 23
    
    numbers_iter = iter(numbers_iter)
    
    numbers_iter *= 24
    
    numbers_iter = iter(numbers_iter)
    
    