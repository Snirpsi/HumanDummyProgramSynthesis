#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and calculates a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    numbers_sum = sum(numbers)
    numbers_average = sum(numbers)/len(numbers)
    print("The sum of numbers is {}".format(numbers_sum))
    print("The average of the numbers is {}".format(numbers_average))
    print("The average of the numbers is {}".format(numbers_average/len(numbers)))
    
