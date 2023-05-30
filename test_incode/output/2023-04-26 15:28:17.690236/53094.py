#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits. """    
    fruits = input("Enter the fruits: ")
    fruits = fruits.split()
    fruits = [x.lower() for x in fruits]
    fruits = [x for x in fruits if x not in 'aeiou']
    fruits.sort()
    print("The fruits are " + str(fruits))
    
