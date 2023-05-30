#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words or calculates a list of numbers. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == "":
            continue
        
        words = line.split(" ")
        
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == "":
            continue
        
        numbers = line.split(" ")
        
    numbers = map(int, numbers)
    
    numbers = list(set(numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    numbers = list(map(lambda x: x // 2, numbers))
    
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    