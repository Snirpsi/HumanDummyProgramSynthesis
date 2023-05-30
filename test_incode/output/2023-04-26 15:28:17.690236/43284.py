#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    import sys
    
    numbers = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers_sum = sum(numbers)
    
    print("The sum of all the numbers is {}".format(numbers_sum))
    
