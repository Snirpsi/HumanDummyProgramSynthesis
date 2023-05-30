#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or calculates a list of words. """    
    
    fruit = input("Enter a fruit: ")
    
    fruits = []
    
    while True:
        fruits.append(fruit)
        fruit = input("Enter a fruit: ")
    
    fru