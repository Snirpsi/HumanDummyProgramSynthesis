#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts fruits and enumerates user input. """    
    
    fruit = input("Enter a fruit: ")
    
    fruits = enumerate(fruit)
    
    for index, value in fruits:
        print("The fruit is", value)
    
