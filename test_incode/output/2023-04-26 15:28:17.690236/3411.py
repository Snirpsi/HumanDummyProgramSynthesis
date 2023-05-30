#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and adds user input. """    
    
    fruits = input("Enter fruit names: ")
    
    for fruit in fruits.split():
        print("Fruit " + fru