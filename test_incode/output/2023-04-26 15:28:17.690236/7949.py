#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    import sys
    
    numbers = [int(i) for i in sys.argv[1:]]
    
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
    
    print(numbers)
    
