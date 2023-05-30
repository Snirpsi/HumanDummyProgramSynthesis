#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers and adds user input. """    
    
    numbers = input("Enter a list of numbers: ")
    numbers = [int(i) for i in numbers.split()]
    
    numbers += [int(i) for i in input("Enter the sum of the numbers: ").split()]
    
    print("The sum of the numbers is " + str(sum(numbers)))
    
