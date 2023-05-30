#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or adds fruits. """    
    
    fruits = input("Enter fruits: ")
    
    fruits = fruits.split()
    
    for fruit in fruits:
        if fruit not in 