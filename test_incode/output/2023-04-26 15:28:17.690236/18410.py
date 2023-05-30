#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and converts fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        fruits = [x * 