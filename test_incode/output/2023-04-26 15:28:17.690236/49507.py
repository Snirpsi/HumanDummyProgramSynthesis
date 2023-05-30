#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = map(int, numbers)
    
    numbers = list(set(numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))
    
    numbers = list(filter(lambda x: x not in numbers, numbers))