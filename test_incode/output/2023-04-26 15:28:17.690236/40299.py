#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and multiplyes fruits. """    
    fruits = input("Enter fruits: ")
    multiplier = int(input("Enter multiplier: "))
    
    fruits_multiplied = 0
    for fruit in fruits:
        fruits_multiplied += int(fruit) * multiplier
    
    print(fruits_multiplied)
    
