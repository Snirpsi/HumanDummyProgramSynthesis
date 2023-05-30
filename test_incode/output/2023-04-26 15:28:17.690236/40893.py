#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    numbers = [int(x) for x in input().split()]
    
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)
    
    print(numbers)
    
