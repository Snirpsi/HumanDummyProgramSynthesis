#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    
    numbers_sum = sum(numbers)
    
    print("The sum of the numbers is {}".format(numbers_sum))
    
