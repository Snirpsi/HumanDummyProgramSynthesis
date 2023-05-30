#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and returns fruits. """    
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    fruits = list(fruits)
    fruits.sort()
    print(fruits)
    
