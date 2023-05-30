#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or stores fruits. """    
    
    fruits = input("Enter your fruit names: ")
    
    if fruits:
        fruits = fruits.split()
        
        for fruit in fruits:
            