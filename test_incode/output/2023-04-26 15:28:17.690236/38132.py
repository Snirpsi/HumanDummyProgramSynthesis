#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits or converts a list of numbers. """    
    fruit = input("Enter a fruit or a list of numbers: ")
    fruits = fruit.split()
    
    for fruit in fruits:
        print(fruit)
        
