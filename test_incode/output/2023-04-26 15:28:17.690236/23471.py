#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and calculates fruits. """    
    
    numbers = input("Enter numbers: ")
    fruits = sum(int(i) for i in numbers.split())
    print("The sum of all numbers is {}.".format(fruits))
    
