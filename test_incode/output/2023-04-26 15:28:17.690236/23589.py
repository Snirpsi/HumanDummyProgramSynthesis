#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print("Usage: %s <numbers>" % sys.argv[0])
        exit(1)
    
    numbers = list(map(int, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 3 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 5 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 7 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 9 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 11 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 13 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 15 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 17 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 19 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 21 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 23 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 25 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 27 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 29 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 31 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 33 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 35 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 37 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 39 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 41 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 43 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 45 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 47 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 49 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 51 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 53 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 55 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 57 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 59 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 61 == 0, numbers))
    
    numbers = list(filter(lambda x: x % 63 == 0, number