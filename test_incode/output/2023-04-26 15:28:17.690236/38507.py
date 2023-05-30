#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits or enumerates words. """    
    
    fruit = input("Enter a fruit: ")
    
    fruit = fruit.upper()
    
    fruits = enumerate(fruit)
    
    for fruit in fruits:
        print("The fruit is", fruit)
    
