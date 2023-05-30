#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    numbers_sum = 0
    
    for number in numbers:
        numbers_sum += number
    
    print("The sum of the numbers is {}".format(numbers_sum))
    
