#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input and converts fruits. """    
    
    fruits = input("Enter the fruits: ")
    
    fruits = fruits.split()
    
    for fruit in fruits:
        print("The fruit is", fruit)
        
