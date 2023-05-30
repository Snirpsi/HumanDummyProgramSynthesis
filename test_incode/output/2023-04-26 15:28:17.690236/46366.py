#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and enumerates fruits. """    
    numbers = input("Enter a list of numbers: ")
    fruits = input("Enter a list of fruits: ")
    
    numbers = numbers.split()
    fruits = fruits.split()
    
    fruits.sort()
    numbers.sort()
    
    for number in numbers:
        if number in fruits:
            print(number)
        else:
            print("Not a fruit!")
            
    for fruit in fruits:
        if fruit in numbers:
            print(fruit)
        else:
            print("Not a number!")
            
