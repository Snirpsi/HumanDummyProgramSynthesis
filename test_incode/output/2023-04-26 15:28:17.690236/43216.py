#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and stores fruits. """    
    
    fruits = input("Enter fruits: ")
    
    for fruit in fruits.split():
        print(fruit)
    
